#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================================================
# FlipFX - Character flipping effect text printer
# Copyright (C) 2019 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/flipfx
# GitLab: https://gitlab.com/urbanware-org/flipfx
# ============================================================================

__version__ = "1.0.0"

import random
import time


def charflip(string, delay=0.08):
    """
        {key: value for key, value in variable}
    """
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    string_output = ""
    string_temp = ""

    for i in range(len(string)):
        string_output += random.choice(chars)
    string_range = len(string_output)
    print("\r" + string_output, end='')

    char_list = []
    for i in string_output:
        char_list.append(chars)

    while not string_output == string:
        for i in range(string_range):
            if string[i] not in chars:
                char = string[i]
            elif string_output[i] is not string[i]:
                random.seed()
                chars = char_list[i]
                index = random.randint(0, len(chars) - 1)
                char = chars[index]
                char_list[i] = char_list[i].replace(char, "")
            else:
                char = string_output[i]
            string_temp += char
        string_output = string_temp
        string_temp = ""
        time.sleep(delay)
        print("\r" + string_output, end='')

# EOF
