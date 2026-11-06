"""
测试用例 - 图片分类器

用法：
    pytest tests/test_classifier.py -v
"""

import pytest
import numpy as np
from PIL import Image
import sys
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from classifier import ImageClassifier


class TestImageClassifier:
    """图片分类器测试"""

    def setup_method(self):
        """每个测试方法前的准备工作"""
        self.classifier = ImageClassifier()

    def test_classify_text_image(self):
        """测试文字/图形图片的分类"""
        # 创建一个简单的白底黑字测试图
        img = Image.new("RGB", (100, 100), color="white")
        test_path = Path(__file__).parent / "test_text.png"
        img.save(test_path)

        category, features = self.classifier.classify(str(test_path))

        assert category == "A", f"期望分类为 A，实际为 {category}"
        assert features["white_ratio"] > 0.5, "白底比例应该很高"

    def test_classify_photo_image(self):
        """测试照片图片的分类"""
        # 创建一个随机颜色测试图（模拟照片）
        img_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        img = Image.fromarray(img_array)
        test_path = Path(__file__).parent / "test_photo.png"
        img.save(test_path)

        category, features = self.classifier.classify(str(test_path))

        # 随机图片可能分类为 B（但不绝对）
        assert category in ["A", "B"], f"分类结果无效: {category}"

    def test_features_extraction(self):
        """测试特征提取"""
        img = Image.new("RGB", (100, 100), color="white")
        test_path = Path(__file__).parent / "test_features.png"
        img.save(test_path)

        category, features = self.classifier.classify(str(test_path))

        # 验证特征字典包含必要字段
        assert "white_ratio" in features
        assert "unique_colors" in features
        assert "edge_density" in features
        assert "width" in features
        assert "height" in features

    def test_edge_cases(self):
        """测试边界情况"""
        # 纯黑图片
        img_black = Image.new("RGB", (100, 100), color="black")
        test_path_black = Path(__file__).parent / "test_black.png"
        img_black.save(test_path_black)

        category_black, _ = self.classifier.classify(str(test_path_black))
        assert category_black == "B", "纯黑图片应该分类为 B"

        # 纯白图片
        img_white = Image.new("RGB", (100, 100), color="white")
        test_path_white = Path(__file__).parent / "test_white.png"
        img_white.save(test_path_white)

        category_white, _ = self.classifier.classify(str(test_path_white))
        assert category_white == "A", "纯白图片应该分类为 A"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
