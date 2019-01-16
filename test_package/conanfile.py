#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, tools, CMake
import os


class TestPackageConan(ConanFile):    
    generators = "cmake_find_package"
    def build(self):
        pass

    def test(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()
