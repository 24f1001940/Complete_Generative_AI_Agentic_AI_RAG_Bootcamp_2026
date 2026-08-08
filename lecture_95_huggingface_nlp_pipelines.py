from __future__ import annotations

import importlib.util
import sys


def main() -> None:
    try:
        from transformers import pipeline
        from transformers.pipelines import PIPELINE_REGISTRY
    except Exception as exc:
        print("Could not import transformers.")
        print("Install with: pip install -U transformers torch sentencepiece")
        print(f"Import error: {exc}")
        retlurn

    torch_available = importlib.util.find_spec("torch") is not None
    supported_tasks = set(PIPELINE_REGISTRY.get_supported_tasks())

    if not torch_available:
        print("PyTorch is not installed, so model pipelines cannot run in this environment.")
        print("Install dependencies and re-run:")
        print("  python -m pip install -U pip")
        print("  python -m pip install torch transformers sentencepiece")
        print("Tip: If pip is missing, run: python -m ensurepip --upgrade")
        return

    def require_task(task_name: str) -> bool:
        if task_name in supported_tasks:
            return True
        print(f"Task '{task_name}' is not available in this Transformers build.")
        return False

    print("=" * 20, "Sentiment Analysis", "=" * 20)
    try:
        sentiment_task = "sentiment-analysis" if "sentiment-analysis" in supported_tasks else "text-classification"
        if not require_task(sentiment_task):
            raise RuntimeError("No compatible classification task found.")
        sentiment = pipeline(
            sentiment_task,
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        )
        samples = [
            "The lecture was clear and practical.",
            "The product update broke my workflow.",
        ]
        for text in samples:
            print("Input:", text)
            print("Output:", sentiment(text))
    except Exception as exc:
        print(f"Sentiment example failed: {exc}")

    print("\n" + "=" * 20, "Summarization", "=" * 20)
    try:
        long_text = (
            "Hugging Face pipelines make NLP tasks fast to prototype in real applications. "
            "Teams can combine sentiment, summarization, and translation to process customer feedback. "
            "With batching, caching, and monitoring, this setup can scale for production workflows."
        )

        if "summarization" in supported_tasks:
            summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
            summary = summarizer(long_text, max_length=50, min_length=15, do_sample=False)
            out_text = summary[0].get("summary_text", str(summary[0]))
        elif "text-generation" in supported_tasks:
            generator = pipeline("text-generation", model="gpt2")
            prompt = (
                "Summarize this in one short paragraph:\n"
                f"{long_text}\n\nSummary:"
            )
            gen = generator(prompt, max_new_tokens=60, do_sample=False)
            out_text = gen[0]["generated_text"].split("Summary:", 1)[-1].strip()
        elif "any-to-any" in supported_tasks:
            any_to_any = pipeline("any-to-any", model="google/flan-t5-small")
            out = any_to_any(f"Summarize: {long_text}")
            out_text = str(out)
        else:
            raise RuntimeError("No supported task for summarization in this environment.")

        print("Input:", long_text)
        print("Output:", out_text)
    except Exception as exc:
        print(f"Summarization example failed: {exc}")

    print("\n" + "=" * 20, "Translation EN -> FR", "=" * 20)
    try:
        text = "Artificial Intelligence is transforming how we work."

        if "translation" in supported_tasks:
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
            translated = translator(text)
            out_text = translated[0].get("translation_text", str(translated[0]))
        elif "text2text-generation" in supported_tasks:
            translator = pipeline("text2text-generation", model="Helsinki-NLP/opus-mt-en-fr")
            translated = translator(text, max_new_tokens=64)
            out_text = translated[0].get("generated_text", str(translated[0]))
        elif "any-to-any" in supported_tasks:
            any_to_any = pipeline("any-to-any", model="google/flan-t5-small")
            out = any_to_any(f"Translate to French: {text}")
            out_text = str(out)
        elif "text-generation" in supported_tasks:
            generator = pipeline("text-generation", model="gpt2")
            prompt = f"Translate this sentence to French: {text}\nFrench:"
            gen = generator(prompt, max_new_tokens=50, do_sample=False)
            out_text = gen[0]["generated_text"].split("French:", 1)[-1].strip()
        else:
            raise RuntimeError("No supported task for translation in this environment.")

        print("Input:", text)
        print("Output:", out_text)
    except Exception as exc:
        print(f"Translation example failed: {exc}")

    print("\nSupported tasks in this environment:")
    print(sorted(supported_tasks))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
