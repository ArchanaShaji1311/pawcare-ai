import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { PawPrint, AlertCircle } from "lucide-react";

function LinkedinIcon() {
  return (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
      <path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.07 2.07 0 1 1 0-4.14 2.07 2.07 0 0 1 0 4.14zM7.12 20.45H3.55V9h3.57v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.55C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.72C24 .77 23.2 0 22.22 0z" />
    </svg>
  );
}

function GithubIcon() {
  return (
    <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
      <path d="M12 .3a12 12 0 0 0-3.79 23.4c.6.11.82-.26.82-.58l-.01-2.05c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.09-.75.08-.73.08-.73 1.2.09 1.84 1.24 1.84 1.24 1.07 1.83 2.81 1.3 3.5.99.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.34-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.13-.3-.54-1.52.12-3.18 0 0 1-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.28-1.55 3.29-1.23 3.29-1.23.66 1.66.24 2.88.12 3.18.77.84 1.23 1.91 1.23 3.22 0 4.61-2.8 5.62-5.48 5.92.43.37.81 1.1.81 2.22l-.01 3.29c0 .32.21.7.82.58A12 12 0 0 0 12 .3z" />
    </svg>
  );
}
import Header from "./components/Header";
import Hero from "./components/Hero";
import HowItWorks from "./components/HowItWorks";
import UploadPanel from "./components/UploadPanel";
import ResultsView from "./components/ResultsView";
import ResultsSkeleton from "./components/ResultsSkeleton";
import PageSkeleton from "./components/PageSkeleton";
import { analyzeDog } from "./api";
import { useTheme } from "./useTheme";
import type { AnalyzeResponse } from "./types";

export default function App() {
  const { isDark, toggleTheme } = useTheme();
  const [booting, setBooting] = useState(true);
  const [result, setResult] = useState<AnalyzeResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const timer = setTimeout(() => setBooting(false), 900);
    return () => clearTimeout(timer);
  }, []);

  async function handleAnalyze(data: {
    image: File;
    symptoms: string;
    breed: string;
  }) {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await analyzeDog(data);
      setResult(res);
      setTimeout(
        () =>
          document
            .getElementById("results")
            ?.scrollIntoView({ behavior: "smooth", block: "start" }),
        100,
      );
    } catch (e) {
      setError(e instanceof Error ? e.message : "Analysis failed.");
    } finally {
      setLoading(false);
    }
  }

  if (booting) {
    return <PageSkeleton />;
  }

  return (
    <motion.div
      className="min-h-screen"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.4, ease: "easeOut" }}
    >
      <Header isDark={isDark} onToggleTheme={toggleTheme} />
      <Hero />
      <HowItWorks />

      <section id="analyze" className="max-w-6xl mx-auto px-5 pb-20 scroll-mt-24">
        <div className="grid lg:grid-cols-2 gap-6 items-start">
          <div className="lg:sticky lg:top-24 min-w-0">
            <UploadPanel onAnalyze={handleAnalyze} loading={loading} />
          </div>

          <div id="results" className="min-w-0">
            <AnimatePresence mode="wait">
              {error && (
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="rounded-2xl border border-red-200 dark:border-red-500/30 bg-red-50 dark:bg-red-500/10 p-5 flex items-center gap-3 text-red-700 dark:text-red-300"
                >
                  <AlertCircle size={22} />
                  <p className="font-medium">{error}</p>
                </motion.div>
              )}

              {loading && (
                <motion.div
                  key="loading"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                >
                  <div className="flex items-center justify-center gap-2 text-sm font-medium text-brand-600 dark:text-brand-400 mb-4">
                    <span className="animate-float text-2xl">🐾</span>
                    Analyzing your dog's health…
                  </div>
                  <ResultsSkeleton />
                </motion.div>
              )}

              {!loading && result && <ResultsView key="result" data={result} />}

              {!loading && !result && !error && (
                <motion.div
                  key="empty"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  className="rounded-3xl border-2 border-dashed border-slate-200 dark:border-slate-700 p-10 grid place-items-center text-center text-slate-400 dark:text-slate-500 h-full min-h-[320px]"
                >
                  <div>
                    <span className="grid place-items-center w-14 h-14 rounded-2xl bg-brand-50 dark:bg-brand-500/15 text-brand-400 mx-auto mb-3">
                      <PawPrint size={26} />
                    </span>
                    <p className="font-medium text-slate-500 dark:text-slate-400">
                      Your results will appear here
                    </p>
                    <p className="text-sm mt-1">
                      Upload a photo and click Analyze to begin.
                    </p>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </section>

      <footer className="border-t border-slate-200 dark:border-slate-800 bg-white/60 dark:bg-slate-900/60">
        <div className="max-w-6xl mx-auto px-5 py-6 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="text-center sm:text-left">
            <div className="flex items-center justify-center sm:justify-start gap-2 font-semibold text-slate-700 dark:text-slate-200">
              <PawPrint size={18} className="text-brand-600 dark:text-brand-400" /> PawCare AI
            </div>
            <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
              Informational use only — always consult a licensed veterinarian.
            </p>
            <p className="text-xs text-slate-400 dark:text-slate-500 mt-1">
              © {new Date().getFullYear()} PawCare AI · Built by Archana Shaji. All rights reserved.
            </p>
          </div>

          <div className="flex items-center gap-3">
            <a
              href="https://www.linkedin.com/in/archanashaji1311/"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="LinkedIn"
              className="grid place-items-center w-10 h-10 rounded-full border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:text-white hover:bg-brand-600 hover:border-brand-600 transition"
            >
              <LinkedinIcon />
            </a>
            <a
              href="https://github.com/ArchanaShaji1311/"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="GitHub"
              className="grid place-items-center w-10 h-10 rounded-full border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:text-white hover:bg-brand-600 hover:border-brand-600 transition"
            >
              <GithubIcon />
            </a>
          </div>
        </div>
      </footer>
    </motion.div>
  );
}
