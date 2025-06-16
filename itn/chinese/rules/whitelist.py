# Copyright (c) 2022 Xingchen Song (sxc19@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tn.processor import Processor
from tn.utils import get_abs_path

from pynini import string_file
from pynini.lib.pynutil import insert


class Whitelist(Processor):

    def __init__(self):
        super().__init__(name='whitelist')
        self.build_tagger()
        self.build_verbalizer()

    def build_tagger(self):
        # print("走白名单")
        whitelist = string_file(
            get_abs_path('../itn/chinese/data/default/whitelist.tsv'))

        tagger = insert('value: "') + whitelist + insert('"')
        self.tagger = self.add_tokens(tagger)

        # debug
        # print("[DEBUG] 开始构建白名单 tagger...")
        
        # # 1. 获取白名单文件路径
        # whitelist_path = get_abs_path('../itn/chinese/data/default/whitelist.tsv')
        # print(f"[DEBUG] 白名单文件路径: {whitelist_path}")
        
        # # 2. 检查文件是否存在
        # import os
        # if not os.path.exists(whitelist_path):
        #     print(f"[ERROR] 文件不存在: {whitelist_path}")
        #     raise FileNotFoundError(f"白名单文件未找到: {whitelist_path}")
        # else:
        #     print("[DEBUG] 白名单文件存在，继续加载...")

        # # 3. 打印文件内容（检查实际加载的词汇）
        # with open(whitelist_path, 'r', encoding='utf-8') as f:
        #     lines = f.read().splitlines()
        #     print(f"[DEBUG] 文件行数（词汇数量）: {len(lines)}")
        #     print("[DEBUG] 前10行词汇示例（如果有）:")
        #     for i, line in enumerate(lines[:10]):
        #         print(f"  {i+1}. {line}")

        # # 4. 加载白名单到 pynini FST
        # try:
        #     whitelist = string_file(whitelist_path)
        #     print("[DEBUG] string_file 加载成功！")
        # except Exception as e:
        #     print(f"[ERROR] string_file 加载失败: {e}")
        #     raise

        # # 5. 测试新增词汇是否能匹配（例如："新词汇"）
        # test_word = "新词汇"  # 替换为你新增的词汇
        # try:
        #     from pynini import accep
        #     test_fst = accep(test_word)
        #     matched_fst = test_fst @ whitelist  # 尝试匹配
        #     if matched_fst.num_states() > 0:
        #         print(f"[DEBUG] 测试词汇 '{test_word}' 匹配成功！")
        #     else:
        #         print(f"[WARNING] 测试词汇 '{test_word}' 未匹配！请检查拼写或文件内容。")
        # except Exception as e:
        #     print(f"[WARNING] 无法测试 FST 匹配: {e}")

        # # 6. 构建 tagger
        # tagger = insert('value: "') + whitelist + insert('"')
        # print("[DEBUG] Tagger 构建完成！")
        
        # self.tagger = self.add_tokens(tagger)     