#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os 


class LuaConan(ConanFile):
    name = "lua"
    version = "5.3.5"
    description = """Lua is a powerful, efficient, lightweight, embeddable scripting language. 
    It supports procedural programming, object-oriented programming, functional programming, data-driven programming, and data description."""

    topics = ("conan", "lua", "embeddable")
    url = "https://github.com/ss1978/conan-lua.git"
    homepage = "https://www.lua.org"
    author = ""
    license = "MIT"
    requires = "readline/7.0@bincrafters/stable"
    exports = ["LICENSE.md"]
    settings = "os_build", "compiler", "arch_build"
    options = {
        "tests": [True, False]
    }

    default_options = {
        "tests": False
    }

    _download_url = "https://www.lua.org/ftp/lua-%s.tar.gz" % version
    _sha1 = "112eb10ff04d1b4c9898e121d6bdf54a81482447"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        tools.get(self._download_url, sha1=self._sha1)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        build_folder = os.path.abspath(self._build_subfolder)
        with tools.chdir(os.path.abspath(self._source_subfolder)):
            args = [{
                "Linux": "linux",
                "Windows": "mingw"
            }[self.settings.os_build.value]]
            env_build = AutoToolsBuildEnvironment(self)
            args.append('MYLDFLAGS=%s' % env_build.vars["LDFLAGS"])
            args.append('MYLIBS=%s' % env_build.vars["LIBS"])
            env_build.make(args=args)
            env_build.make(args=['install',"INSTALL_TOP=%s"%build_folder])

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*", dst="bin", src=os.path.join(self._build_subfolder, "bin"))
        self.copy("*", dst="lib", src=os.path.join(self._build_subfolder, "lib"))
        self.copy("*", dst="include", src=os.path.join(self._build_subfolder, "include"))

    def package_id(self):
        del self.info.settings.compiler

    def package_info(self):
        self.cpp_info.libs.append("lua")
