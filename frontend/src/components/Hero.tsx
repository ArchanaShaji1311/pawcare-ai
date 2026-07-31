import { motion } from "framer-motion";
import { ShieldCheck, ScanEye, HeartPulse, Sparkles } from "lucide-react";

const features = [
  { icon: ScanEye, label: "Image analysis" },
  { icon: HeartPulse, label: "Symptom triage" },
  { icon: ShieldCheck, label: "Vet-safe alerts" },
];

export default function Hero() {
  return (
    <section
      id="top"
      className="relative overflow-hidden min-h-[calc(100vh-4rem)] flex items-center"
    >
      <div className="paw-grid absolute inset-0 -z-10" />
      <div className="max-w-6xl mx-auto px-5 py-16 grid md:grid-cols-2 gap-12 lg:gap-16 items-center w-full">
        <div>
          <motion.span
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-brand-100 dark:bg-brand-500/15 text-brand-700 dark:text-brand-300 text-sm font-semibold"
          >
            <Sparkles size={16} /> Powered by Gemini Vision AI
          </motion.span>
          <motion.h1
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.05 }}
            className="mt-6 text-5xl sm:text-6xl lg:text-7xl font-extrabold leading-[1.05] tracking-tight text-slate-900 dark:text-white"
          >
            Understand your dog's
            <span className="block bg-gradient-to-r from-brand-600 to-accent-500 dark:from-brand-400 dark:to-accent-400 bg-clip-text text-transparent">
              health in seconds
            </span>
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.12 }}
            className="mt-6 text-lg sm:text-xl leading-relaxed text-slate-600 dark:text-slate-300 max-w-xl"
          >
            Upload a photo, describe the symptoms, and get an AI-assisted read on
            allergies, skin infections, wounds and behavior — with breed-specific
            care and honest vet-consultation alerts.
          </motion.p>
          <motion.div
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.18 }}
            className="mt-8 flex flex-wrap items-center gap-4"
          >
            <a
              href="#analyze"
              className="px-7 py-3.5 text-base rounded-full bg-brand-600 text-white font-semibold shadow-lg shadow-brand-600/30 hover:bg-brand-700 hover:-translate-y-0.5 transition"
            >
              Analyze my dog
            </a>
            <a
              href="#how"
              className="px-7 py-3.5 text-base rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-semibold border border-slate-200 dark:border-slate-700 hover:border-brand-300 dark:hover:border-brand-500 transition"
            >
              See how it works
            </a>
          </motion.div>
          <div className="mt-10 flex flex-wrap gap-x-8 gap-y-3">
            {features.map((f) => (
              <div
                key={f.label}
                className="flex items-center gap-2 text-base text-slate-600 dark:text-slate-400"
              >
                <f.icon size={20} className="text-brand-600 dark:text-brand-400" />
                {f.label}
              </div>
            ))}
          </div>
        </div>

        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.1 }}
          className="relative"
        >
          <div className="animate-float relative mx-auto w-full max-w-md">
            <div className="absolute -inset-5 bg-gradient-to-tr from-brand-300/40 to-accent-400/30 blur-3xl rounded-[2.5rem]" />
            <div className="relative rounded-[2.5rem] bg-white dark:bg-slate-800 shadow-2xl shadow-brand-900/10 dark:shadow-black/40 p-7 border border-brand-100 dark:border-slate-700">
              <div className="rounded-2xl h-64 bg-gradient-to-br from-brand-100 to-sand-100 dark:from-brand-500/20 dark:to-accent-500/10 grid place-items-center text-8xl">
                🐕
              </div>
              <div className="mt-5 space-y-4">
                <div className="flex items-center justify-between text-base">
                  <span className="font-semibold text-slate-700 dark:text-slate-200">
                    Skin health
                  </span>
                  <span className="text-brand-600 dark:text-brand-400 font-bold text-lg">92%</span>
                </div>
                <div className="h-2.5 rounded-full bg-slate-100 dark:bg-slate-700 overflow-hidden">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: "92%" }}
                    transition={{ delay: 0.5, duration: 0.8 }}
                    className="h-full rounded-full bg-brand-500"
                  />
                </div>
                <div className="flex items-center gap-2 text-sm text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 rounded-xl px-3 py-2.5">
                  <ShieldCheck size={16} /> No urgent concerns detected
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
