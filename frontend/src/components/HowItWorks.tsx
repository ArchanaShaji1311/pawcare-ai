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
    <section id="how" className="max-w-6xl mx-auto px-5 py-14">
      <div className="text-center max-w-2xl mx-auto">
        <h2 className="text-3xl font-extrabold text-slate-900">How it works</h2>
        <p className="text-slate-500 mt-2">
          Thoughtful, ethical AI that supports — never replaces — your veterinarian.
        </p>
      </div>
      <div className="mt-10 grid md:grid-cols-3 gap-5">
        {steps.map((s, i) => (
          <div
            key={s.title}
            className="relative rounded-3xl bg-white border border-slate-100 p-6 shadow-sm hover:shadow-lg hover:-translate-y-1 transition"
          >
            <span className="absolute -top-3 -left-3 grid place-items-center w-9 h-9 rounded-xl bg-accent-500 text-white font-bold shadow-lg">
              {i + 1}
            </span>
            <span className="grid place-items-center w-12 h-12 rounded-2xl bg-brand-100 text-brand-600 mb-4">
              <s.icon size={24} />
            </span>
            <h3 className="font-bold text-slate-800 text-lg">{s.title}</h3>
            <p className="text-slate-600 mt-1.5 text-sm">{s.text}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
