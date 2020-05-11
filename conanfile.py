from conans import ConanFile, CMake, tools


class FmtConan(ConanFile):
    name = "jwt-cpp"
    version = "0.4.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of jwt-cpp here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "use_pic": [True, False]
    }
    default_options = {"shared": False, "use_pic": False}
    requires = [
        "openssl/1.1.1f@bitwyre/stable"
    ]
    generators = "cmake"
    exports_sources = "*"
    no_copy_source = True

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.definitions['BUILD_TESTING'] = False
        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.use_pic
        cmake.definitions['BUILD_TESTS'] = False
        cmake.definitions['EXTERNAL_PICOJSON'] = False
        cmake.definitions['OPENSSL_ROOT_DIR'] = self.deps_cpp_info["openssl"].rootpath
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
