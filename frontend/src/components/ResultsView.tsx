import { useState } from "react";
import { motion } from "framer-motion";
import {
  AlertTriangle,
  Bone,
  Activity,
  Stethoscope,
  CheckCircle2,
  Sparkles,
  Info,
  Library,
} from "lucide-react";
import type { AnalyzeResponse, DetectedCondition } from "../types";

const severityStyle: Record<string, string> = {
  none: "bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300",
  mild: "bg-amber-100 dark:bg-amber-500/15 text-amber-700 dark:text-amber-300",
  moderate: "bg-orange-100 dark:bg-orange-500/15 text-orange-700 dark:text-orange-300",
  severe: "bg-red-100 dark:bg-red-500/15 text-red-700 dark:text-red-300",
};

const urgencyStyle: Record<string, { bg: string; text: string; label: string }> = {
  urgent: {
    bg: "bg-red-50 dark:bg-red-500/10 border-red-200 dark:border-red-500/30",
    text: "text-red-700 dark:text-red-300",
    label: "See a vet urgently",
  },
  soon: {
    bg: "bg-orange-50 dark:bg-orange-500/10 border-orange-200 dark:border-orange-500/30",
    text: "text-orange-700 dark:text-orange-300",
    label: "Schedule a vet visit soon",
  },
  routine: {
    bg: "bg-amber-50 dark:bg-amber-500/10 border-amber-200 dark:border-amber-500/30",
    text: "text-amber-700 dark:text-amber-300",
    label: "Mention at your next vet visit",
  },
  none: {
    bg: "bg-emerald-50 dark:bg-emerald-500/10 border-emerald-200 dark:border-emerald-500/30",
    text: "text-emerald-700 dark:text-emerald-300",
    label: "No urgent concerns",
  },
};

function ConfidenceBar({ value }: { value: number }) {
  const pct = Math.round(value * 100);
  const color =
    pct >= 75 ? "bg-emerald-500" : pct >= 50 ? "bg-amber-500" : "bg-slate-400";
  return (
    <div className="flex items-center gap-2 w-32">
      <div className="flex-1 h-2 rounded-full bg-slate-100 dark:bg-slate-700 overflow-hidden">
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${pct}%` }}
          transition={{ duration: 0.7 }}
          className={`h-full rounded-full ${color}`}
        />
      </div>
      <span className="text-xs font-semibold text-slate-500 dark:text-slate-400 w-9 text-right">
        {pct}%
      </span>
    </div>
  );
}

function ConditionCard({ c }: { c: DetectedCondition }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-slate-100 dark:border-slate-700 bg-white dark:bg-slate-800 p-4 shadow-sm"
    >
      <div className="flex items-start justify-between gap-3">
        <div>
          <p className="font-semibold text-slate-800 dark:text-slate-100">{c.name}</p>
          <span className="text-xs text-slate-400 dark:text-slate-500 capitalize">
            {c.category.replace("_", " ")}
          </span>
        </div>
        <span
          className={`text-xs font-bold px-2.5 py-1 rounded-full capitalize ${
            severityStyle[c.severity] ?? severityStyle.none
          }`}
        >
          {c.severity}
        </span>
      </div>
      <p className="text-sm text-slate-600 dark:text-slate-300 mt-2">{c.explanation}</p>
      <div className="mt-3 flex items-center justify-between">
        <span className="text-xs text-slate-400 dark:text-slate-500">AI confidence</span>
        <ConfidenceBar value={c.confidence} />
      </div>
    </motion.div>
  );
}

const tabs = [
  { key: "diet", label: "Diet", icon: Bone },
  { key: "exercise", label: "Exercise", icon: Activity },
  { key: "medical", label: "Medical", icon: Stethoscope },
] as const;

export default function ResultsView({ data }: { data: AnalyzeResponse }) {
  const [tab, setTab] = useState<(typeof tabs)[number]["key"]>("diet");
  const urgency = urgencyStyle[data.vet_alert.urgency] ?? urgencyStyle.none;
  const recs = data.recommendations[tab];

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="space-y-5"
    >
      <div className="rounded-3xl bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 shadow-xl shadow-slate-900/5 dark:shadow-black/30 p-6 sm:p-8">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-xl font-bold text-slate-900 dark:text-white">Analysis summary</h3>
              <span
                className={`inline-flex items-center gap-1 text-[11px] font-semibold px-2 py-0.5 rounded-full ${
                  data.ai_source !== "fallback"
                    ? "bg-brand-100 dark:bg-brand-500/15 text-brand-700 dark:text-brand-300"
                    : "bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-300"
                }`}
              >
                <Sparkles size={12} />
                {data.ai_source !== "fallback" ? "Frontier Vision" : "Offline mode"}
              </span>
            </div>
            {data.breed && (
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Breed: {data.breed}</p>
            )}
          </div>
          <div className="text-right">
            <p className="text-xs text-slate-400 dark:text-slate-500">Overall confidence</p>
            <p className="text-2xl font-extrabold text-brand-600 dark:text-brand-400">
              {Math.round(data.overall_confidence * 100)}%
            </p>
          </div>
        </div>
        <p className="text-slate-600 dark:text-slate-300 mt-3">{data.overall_summary}</p>
      </div>

      <div className={`rounded-2xl border p-4 flex items-start gap-3 ${urgency.bg}`}>
        {data.vet_alert.triggered ? (
          <AlertTriangle className={urgency.text} size={22} />
        ) : (
          <CheckCircle2 className={urgency.text} size={22} />
        )}
        <div>
          <p className={`font-bold ${urgency.text}`}>{urgency.label}</p>
          {data.vet_alert.reasons.length > 0 && (
            <ul className="mt-1 text-sm text-slate-600 dark:text-slate-300 list-disc list-inside space-y-0.5">
              {data.vet_alert.reasons.map((r, i) => (
                <li key={i}>{r}</li>
              ))}
            </ul>
          )}
        </div>
      </div>

      <div>
        <h4 className="font-bold text-slate-800 dark:text-slate-100 mb-3">
          Detected findings ({data.conditions.length})
        </h4>
        {data.conditions.length === 0 ? (
          <div className="rounded-2xl border border-emerald-100 dark:border-emerald-500/30 bg-emerald-50 dark:bg-emerald-500/10 p-5 flex items-center gap-3 text-emerald-700 dark:text-emerald-300">
            <CheckCircle2 size={22} />
            <p className="font-medium">
              No specific concerns detected. Keep up the great care!
            </p>
          </div>
        ) : (
          <div className="grid sm:grid-cols-2 gap-3">
            {data.conditions.map((c, i) => (
              <ConditionCard key={i} c={c} />
            ))}
          </div>
        )}
      </div>

      <div className="rounded-3xl bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 shadow-lg shadow-slate-900/5 dark:shadow-black/30 p-6">
        <h4 className="font-bold text-slate-800 dark:text-slate-100 mb-4">Personalized care plan</h4>
        <div className="flex flex-wrap gap-2 mb-4">
          {tabs.map((t) => (
            <button
              key={t.key}
              onClick={() => setTab(t.key)}
              className={`flex items-center gap-1.5 px-4 py-2 rounded-full text-sm font-semibold transition ${
                tab === t.key
                  ? "bg-brand-600 text-white shadow-md shadow-brand-600/25"
                  : "bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-600"
              }`}
            >
              <t.icon size={16} /> {t.label}
            </button>
          ))}
        </div>
        <div className="space-y-3">
          {recs.map((r, i) => (
            <motion.div
              key={`${tab}-${i}`}
              initial={{ opacity: 0, x: -8 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: i * 0.04 }}
              className="flex gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-900/50"
            >
              <span className="mt-0.5 grid place-items-center w-7 h-7 shrink-0 rounded-lg bg-brand-100 dark:bg-brand-500/15 text-brand-600 dark:text-brand-400">
                <CheckCircle2 size={16} />
              </span>
              <div>
                {r.title && (
                  <p className="font-semibold text-slate-800 dark:text-slate-100 text-sm">
                    {r.title}
                  </p>
                )}
                <p className="text-sm text-slate-600 dark:text-slate-300">{r.detail}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>

      {data.sources.length > 0 && (
        <div className="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400 px-1">
          <Library size={14} className="text-brand-600 dark:text-brand-400 shrink-0" />
          <span>
            Evidence grounded in PawCare's veterinary knowledge base
            (retrieval-augmented).
          </span>
        </div>
      )}

      <div className="flex items-start gap-2 text-xs text-slate-500 dark:text-slate-400 bg-slate-50 dark:bg-slate-800/60 rounded-xl p-4">
        <Info size={16} className="shrink-0 mt-0.5" />
        <p>{data.disclaimer}</p>
      </div>
    </motion.div>
  );
}
