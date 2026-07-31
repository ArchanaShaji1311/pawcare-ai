import { motion } from "framer-motion";
import { ShieldCheck, ScanEye, HeartPulse, Sparkles } from "lucide-react";

const features = [
  { icon: ScanEye, label: "Image analysis" },
  { icon: HeartPulse, label: "Symptom triage" },
  { icon: ShieldCheck, label: "Vet-safe alerts" },
];

const screensFor = ["Allergies", "Skin infections", "Wounds", "Behavior"];

const stats = [
  { value: "10+", label: "Breeds supported" },
  { value: "4", label: "Condition types" },
  { value: "<10s", label: "To results" },
];

export default function Hero() {
  return (
    <section
      id="top"
      className="relative overflow-hidden min-h-[calc(100vh-4rem)] flex items-center"
    >
      <div className="paw-grid absolute inset-0 -z-10" />
      <div className="max-w-6xl mx-auto px-5 py-12 grid md:grid-cols-2 gap-10 lg:gap-14 items-center w-full">
        <div>
          <motion.span
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-100 dark:bg-brand-500/15 text-brand-700 dark:text-brand-300 text-xs font-semibold"
          >
            <Sparkles size={14} /> Powered by Gemini Vision AI
          </motion.span>
          <motion.h1
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.05 }}
            className="mt-4 text-4xl sm:text-5xl font-extrabold leading-tight tracking-tight text-slate-900 dark:text-white"
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
            className="mt-5 text-lg text-slate-600 dark:text-slate-300 max-w-md"
          >
            Upload a photo, describe the symptoms, and get an AI-assisted read on
            allergies, skin infections, wounds and behavior — with breed-specific
            care and honest vet-consultation alerts.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.16 }}
            className="mt-6"
          >
            <p className="text-xs font-semibold uppercase tracking-wide text-slate-400 dark:text-slate-500 mb-2">
              Screens for
            </p>
            <div className="flex flex-wrap gap-2">
              {screensFor.map((s) => (
                <span
                  key={s}
                  className="px-3 py-1 rounded-full text-sm font-medium bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300"
                >
                  {s}
                </span>
              ))}
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="mt-7 flex flex-wrap items-center gap-3"
          >
            <a
              href="#analyze"
              className="px-6 py-3 rounded-full bg-brand-600 text-white font-semibold shadow-lg shadow-brand-600/30 hover:bg-brand-700 hover:-translate-y-0.5 transition"
            >
              Analyze my dog
            </a>
            <a
              href="#how"
              className="px-6 py-3 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-semibold border border-slate-200 dark:border-slate-700 hover:border-brand-300 dark:hover:border-brand-500 transition"
            >
              See how it works
            </a>
          </motion.div>

          <div className="mt-8 flex gap-6">
            {features.map((f) => (
              <div
                key={f.label}
                className="flex items-center gap-2 text-sm text-slate-600 dark:text-slate-400"
              >
                <f.icon size={18} className="text-brand-600 dark:text-brand-400" />
                {f.label}
              </div>
            ))}
          </div>

          <div className="mt-8 pt-6 border-t border-slate-200 dark:border-slate-800 flex gap-8">
            {stats.map((s) => (
              <div key={s.label}>
                <p className="text-2xl font-extrabold text-slate-900 dark:text-white">
                  {s.value}
                </p>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                  {s.label}
                </p>
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
            <div className="absolute -inset-6 bg-gradient-to-tr from-brand-300/40 to-accent-400/30 blur-3xl rounded-[2.5rem]" />
            <div className="relative rounded-[2.5rem] bg-white dark:bg-slate-800 shadow-2xl shadow-brand-900/10 dark:shadow-black/40 p-6 sm:p-7 border border-brand-100 dark:border-slate-700">
              <img
                src="/hero-dog.jpg"
                alt="Two healthy, happy golden retriever puppies"
                loading="eager"
                className="rounded-2xl h-60 w-full object-cover"
              />
              <p className="mt-5 text-xs font-semibold uppercase tracking-wide text-slate-400 dark:text-slate-500">
                AI snapshot
              </p>
              <div className="mt-3 space-y-3.5">
                <MetricBar label="Skin health" value={92} delay={0.5} />
                <MetricBar label="Coat & fur" value={88} delay={0.65} />
                <div className="flex items-center gap-2 text-xs text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 rounded-lg px-3 py-2">
                  <ShieldCheck size={14} /> No urgent concerns detected
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}

function MetricBar({
  label,
  value,
  delay,
}: {
  label: string;
  value: number;
  delay: number;
}) {
  return (
    <div>
      <div className="flex items-center justify-between text-sm">
        <span className="font-semibold text-slate-700 dark:text-slate-200">{label}</span>
        <span className="text-brand-600 dark:text-brand-400 font-bold">{value}%</span>
      </div>
      <div className="mt-1 h-2 rounded-full bg-slate-100 dark:bg-slate-700 overflow-hidden">
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${value}%` }}
          transition={{ delay, duration: 0.8 }}
          className="h-full rounded-full bg-brand-500"
        />
      </div>
    </div>
  );
}
