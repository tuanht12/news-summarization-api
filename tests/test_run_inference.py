def test_run_inference():
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    from configs.conf import INFERENCE_CONFIG_PATH
    from src.text_summarizer import TextSummarizer

    sample_text = """Tàu sân bay Queen Elizabeth bị cháy sau khi cập cảng Glenmallan để tháo dỡ đạn dược, chuẩn bị sửa chữa sự cố chân vịt.
                    HMS Queen Elizabeth cập cảng Glenmallan để tháo dỡ đạn dược và nhu yếu phẩm, trước khi tới nhà máy tại Rosyth để sửa chữa trục chân vịt và bảo dưỡng.
                    Phát ngôn viên hải quân Anh xác nhận thông tin, nói rằng "đám cháy nhỏ lẻ" trên HMS Queen Elizabeth đã được kiểm soát và dập tắt nhanh chóng, nhấn mạnh sự cố không liên quan đến kho đạn dược trên tàu."""  # noqa
    text_summarizer = TextSummarizer(inference_config_path=INFERENCE_CONFIG_PATH)
    text_summarizer.summarize(sample_text)
