"""
测试用例 - 图片处理器

用法：
    pytest tests/test_processor.py -v
"""

import pytest
import numpy as np
from PIL import Image
import sys
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from processor import ImageProcessor


class TestImageProcessor:
    """图片处理器测试"""

    def setup_method(self):
        """每个测试方法前的准备工作"""
        self.processor = ImageProcessor(intensity="medium")

    def test_process_class_a(self):
        """测试 A 类图片处理"""
        # 创建白底黑字测试图
        img = Image.new("RGB", (100, 100), color="white")
        test_path = Path(__file__).parent / "test_a_input.png"
        output_path = Path(__file__).parent / "test_a_output.png"
        img.save(test_path)

        result = self.processor.process(
            str(test_path), category="A", output_path=str(output_path)
        )

        assert output_path.exists(), f"输出文件不存在: {result}"

        # 验证输出图片
        result_img = Image.open(result)
        assert result_img.size == (100, 100), "输出尺寸应该保持一致"

    def test_process_class_b(self):
        """测试 B 类图片处理"""
        # 创建彩色测试图
        img_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        img = Image.fromarray(img_array)
        test_path = Path(__file__).parent / "test_b_input.png"
        output_path = Path(__file__).parent / "test_b_output.png"
        img.save(test_path)

        result = self.processor.process(
            str(test_path), category="B", output_path=str(output_path)
        )

        assert output_path.exists(), f"输出文件不存在: {result}"

    def test_different_intensities(self):
        """测试不同强度参数"""
        img = Image.new("RGB", (100, 100), color="white")
        test_path = Path(__file__).parent / "test_intensity.png"
        img.save(test_path)

        for intensity in ["light", "medium", "strong"]:
            processor = ImageProcessor(intensity=intensity)
            output_path = Path(__file__).parent / f"test_{intensity}.png"
            processor.process(
                str(test_path), category="A", output_path=str(output_path)
            )

            assert output_path.exists(), f"{intensity} 强度处理失败"

    def test_auto_category(self):
        """测试自动分类处理"""
        img = Image.new("RGB", (100, 100), color="white")
        test_path = Path(__file__).parent / "test_auto.png"
        output_path = Path(__file__).parent / "test_auto_out.png"
        img.save(test_path)

        result = self.processor.process(
            str(test_path), category="auto", output_path=str(output_path)
        )

        assert output_path.exists(), f"自动分类处理失败: {result}"

    def test_output_path_generation(self):
        """测试输出路径生成"""
        input_path = str(Path(__file__).parent / "test.png")
        expected = str(Path(__file__).parent / "test.dark.png")

        result = ImageProcessor._generate_output_path(input_path)
        assert result == expected, f"期望 {expected}，实际 {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
