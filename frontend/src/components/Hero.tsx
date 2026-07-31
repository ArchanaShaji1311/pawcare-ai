import { motion } from "framer-motion";
import { ShieldCheck, ScanEye, HeartPulse, Sparkles } from "lucide-react";

const features = [
  { icon: ScanEye, label: "Image analysis" },
  { icon: HeartPulse, label: "Symptom triage" },
  { icon: ShieldCheck, label: "Vet-safe alerts" },
];

export default function Hero() {
  return (
    <section id="top" className="relative overflow-hidden">
      <div className="paw-grid absolute inset-0 -z-10" />
      <div className="max-w-6xl mx-auto px-5 pt-16 pb-12 grid md:grid-cols-2 gap-10 items-center">
        <div>
          <motion.span
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-100 text-brand-700 text-xs font-semibold"
          >
            <Sparkles size={14} /> Powered by Gemini Vision AI
          </motion.span>
          <motion.h1
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.05 }}
            className="mt-4 text-4xl sm:text-5xl font-extrabold leading-tight tracking-tight text-slate-900"
          >
            Understand your dog's
            <span className="block bg-gradient-to-r from-brand-600 to-accent-500 bg-clip-text text-transparent">
              health in seconds
            </span>
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.12 }}
            className="mt-5 text-slate-600 text-lg max-w-md"
          >
            Upload a photo, describe the symptoms, and get an AI-assisted read on
            allergies, skin infections, wounds and behavior — with breed-specific
            care and honest vet-consultation alerts.
          </motion.p>
          <motion.div
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.18 }}
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
              className="px-6 py-3 rounded-full bg-white text-slate-700 font-semibold border border-slate-200 hover:border-brand-300 transition"
            >
              See how it works
            </a>
          </motion.div>
          <div className="mt-8 flex gap-6">
            {features.map((f) => (
              <div key={f.label} className="flex items-center gap-2 text-sm text-slate-600">
                <f.icon size={18} className="text-brand-600" />
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
          <div className="animate-float relative mx-auto w-full max-w-sm">
            <div className="absolute -inset-4 bg-gradient-to-tr from-brand-300/40 to-accent-400/30 blur-2xl rounded-[2rem]" />
            <div className="relative rounded-[2rem] bg-white shadow-2xl shadow-brand-900/10 p-6 border border-brand-100">
              <div className="rounded-2xl h-48 bg-gradient-to-br from-brand-100 to-sand-100 grid place-items-center text-7xl">
                🐕
              </div>
              <div className="mt-4 space-y-3">
                <div className="flex items-center justify-between text-sm">
                  <span className="font-semibold text-slate-700">Skin health</span>
                  <span className="text-brand-600 font-bold">92%</span>
                </div>
                <div className="h-2 rounded-full bg-slate-100 overflow-hidden">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: "92%" }}
                    transition={{ delay: 0.5, duration: 0.8 }}
                    className="h-full rounded-full bg-brand-500"
                  />
                </div>
                <div className="flex items-center gap-2 text-xs text-emerald-600 bg-emerald-50 rounded-lg px-3 py-2">
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
