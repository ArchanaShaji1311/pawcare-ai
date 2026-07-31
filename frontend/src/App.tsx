import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { PawPrint, AlertCircle } from "lucide-react";
import Header from "./components/Header";
import Hero from "./components/Hero";
import HowItWorks from "./components/HowItWorks";
import UploadPanel from "./components/UploadPanel";
import ResultsView from "./components/ResultsView";
import { analyzeDog } from "./api";
import type { AnalyzeResponse } from "./types";

export default function App() {
  const [result, setResult] = useState<AnalyzeResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

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

  return (
    <div className="min-h-screen">
      <Header />
      <Hero />
      <HowItWorks />

      <section id="analyze" className="max-w-6xl mx-auto px-5 pb-20">
        <div className="grid lg:grid-cols-2 gap-6 items-start">
          <div className="lg:sticky lg:top-24">
            <UploadPanel onAnalyze={handleAnalyze} loading={loading} />
          </div>

          <div id="results">
            <AnimatePresence mode="wait">
              {error && (
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="rounded-2xl border border-red-200 bg-red-50 p-5 flex items-center gap-3 text-red-700"
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
                  className="rounded-3xl bg-white border border-slate-100 shadow-xl p-10 grid place-items-center text-center"
                >
                  <span className="animate-float text-6xl mb-4">🐾</span>
                  <p className="font-semibold text-slate-700">
                    Analyzing your dog's health…
                  </p>
                  <p className="text-sm text-slate-400 mt-1">
                    Preprocessing image and evaluating symptoms
                  </p>
                </motion.div>
              )}

              {!loading && result && <ResultsView key="result" data={result} />}

              {!loading && !result && !error && (
                <motion.div
                  key="empty"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  className="rounded-3xl border-2 border-dashed border-slate-200 p-10 grid place-items-center text-center text-slate-400 h-full min-h-[320px]"
                >
                  <div>
                    <span className="grid place-items-center w-14 h-14 rounded-2xl bg-brand-50 text-brand-400 mx-auto mb-3">
                      <PawPrint size={26} />
                    </span>
                    <p className="font-medium text-slate-500">
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

      <footer className="border-t border-slate-200 bg-white/60">
        <div className="max-w-6xl mx-auto px-5 py-8 flex flex-col sm:flex-row items-center justify-between gap-3 text-sm text-slate-500">
          <div className="flex items-center gap-2 font-semibold text-slate-700">
            <PawPrint size={18} className="text-brand-600" /> PawCare AI
          </div>
          <p>Informational use only — always consult a licensed veterinarian.</p>
        </div>
      </footer>
    </div>
  );
}
