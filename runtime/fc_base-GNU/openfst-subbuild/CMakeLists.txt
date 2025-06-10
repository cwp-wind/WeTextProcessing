# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.22.1)

# We name the project and the target for the ExternalProject_Add() call
# to something that will highlight to the user what we are working on if
# something goes wrong and an error message is produced.

project(openfst-populate NONE)



include(ExternalProject)
ExternalProject_Add(openfst-populate
                     "UPDATE_DISCONNECTED" "False" "URL" "https://github.com/kkm000/openfst/archive/refs/tags/win/1.7.2.1.tar.gz" "URL_HASH" "SHA256=e04e1dabcecf3a687ace699ccb43a8a27da385777a56e69da6e103344cc66bca" "PATCH_COMMAND" "/usr/bin/cmake" "-E" "copy_directory" "/root/code/wetext_my/runtime/patch/openfst" "/root/code/wetext_my/runtime/fc_base-GNU/openfst-src"
                    SOURCE_DIR          "/root/code/wetext_my/runtime/fc_base-GNU/openfst-src"
                    BINARY_DIR          "/root/code/wetext_my/runtime/fc_base-GNU/openfst-build"
                    CONFIGURE_COMMAND   ""
                    BUILD_COMMAND       ""
                    INSTALL_COMMAND     ""
                    TEST_COMMAND        ""
                    USES_TERMINAL_DOWNLOAD  YES
                    USES_TERMINAL_UPDATE    YES
)


