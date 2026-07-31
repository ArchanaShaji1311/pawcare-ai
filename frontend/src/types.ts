export type Severity = "none" | "mild" | "moderate" | "severe";

export interface DetectedCondition {
  name: string;
  category: string;
  severity: Severity;
  confidence: number;
  explanation: string;
}

export interface Recommendation {
  title: string;
  detail: string;
}

export interface RecommendationSet {
  diet: Recommendation[];
  exercise: Recommendation[];
  medical: Recommendation[];
}

export interface VetAlert {
  triggered: boolean;
  urgency: "none" | "routine" | "soon" | "urgent";
  reasons: string[];
}

export interface Source {
  id: string;
  title: string;
  snippet: string;
}

export interface AnalyzeResponse {
  is_dog: boolean;
  image_quality: string;
  breed: string | null;
  overall_summary: string;
  overall_confidence: number;
  conditions: DetectedCondition[];
  recommendations: RecommendationSet;
  vet_alert: VetAlert;
  sources: Source[];
  ai_source: "gemini" | "fallback";
  disclaimer: string;
}
