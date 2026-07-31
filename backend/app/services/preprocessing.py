import io

from PIL import Image, ImageOps, ImageFilter, ImageStat


class ImageValidationError(Exception):
    pass


def preprocess_image(raw: bytes, max_mb: int, longest_edge: int) -> tuple[bytes, dict]:
    if len(raw) > max_mb * 1024 * 1024:
        raise ImageValidationError(f"Image exceeds {max_mb}MB limit.")

    try:
        image = Image.open(io.BytesIO(raw))
        image.verify()
        image = Image.open(io.BytesIO(raw))
    except Exception as exc:
        raise ImageValidationError("File is not a valid image.") from exc

    image = ImageOps.exif_transpose(image)
    image = image.convert("RGB")

    original_size = image.size

    image.thumbnail((longest_edge, longest_edge), Image.LANCZOS)

    image = ImageOps.autocontrast(image, cutoff=1)

    stat = ImageStat.Stat(image)
    brightness = sum(stat.mean) / len(stat.mean)

    edge_response = _sharpness_score(image)

    quality = _estimate_quality(brightness, edge_response)

    buffer = io.BytesIO()
    image.save(buffer, format="JPEG", quality=90)

    meta = {
        "original_size": original_size,
        "processed_size": image.size,
        "brightness": round(brightness, 1),
        "sharpness": round(edge_response, 1),
        "estimated_quality": quality,
    }
    return buffer.getvalue(), meta


def _sharpness_score(image: Image.Image) -> float:
    gray = image.convert("L")
    edges = gray.filter(ImageFilter.FIND_EDGES)
    return ImageStat.Stat(edges).stddev[0]


def _estimate_quality(brightness: float, sharpness: float) -> str:
    if brightness < 40 or brightness > 225 or sharpness < 8:
        return "poor"
    if brightness < 70 or brightness > 200 or sharpness < 18:
        return "fair"
    return "good"
