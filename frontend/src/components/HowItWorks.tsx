import { Camera, Cpu, ClipboardList } from "lucide-react";

const steps = [
  {
    icon: Camera,
    title: "Upload a photo",
    text: "Snap or drop a clear picture of your dog and add any symptoms you've noticed.",
  },
  {
    icon: Cpu,
    title: "AI analyzes",
    text: "Our vision model and symptom engine scan for allergies, infections, wounds and behavior cues.",
  },
  {
    icon: ClipboardList,
    title: "Get a care plan",
    text: "Receive breed-specific diet, exercise and medical guidance — plus honest vet alerts.",
  },
];

export default function HowItWorks() {
  return (
    <section id="how" className="max-w-6xl mx-auto px-5 py-14 scroll-mt-24">
      <div className="text-center max-w-2xl mx-auto">
        <h2 className="text-3xl font-extrabold text-slate-900 dark:text-white">
          How it works
        </h2>
        <p className="text-slate-500 dark:text-slate-400 mt-2">
          Thoughtful, ethical AI that supports — never replaces — your veterinarian.
        </p>
      </div>
      <div className="mt-10 grid md:grid-cols-3 gap-5">
        {steps.map((s, i) => (
          <div
            key={s.title}
            className="rounded-3xl bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 p-6 shadow-sm hover:shadow-lg dark:hover:shadow-black/40 hover:-translate-y-1 transition"
          >
            <div className="flex items-start justify-between mb-4">
              <span className="grid place-items-center w-12 h-12 rounded-2xl bg-brand-100 dark:bg-brand-500/15 text-brand-600 dark:text-brand-400">
                <s.icon size={24} />
              </span>
              <span className="text-4xl font-extrabold leading-none text-slate-200 dark:text-slate-700 select-none">
                {String(i + 1).padStart(2, "0")}
              </span>
            </div>
            <h3 className="font-bold text-slate-800 dark:text-slate-100 text-lg">
              {s.title}
            </h3>
            <p className="text-slate-600 dark:text-slate-400 mt-1.5 text-sm">{s.text}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
