# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.22.1)

# We name the project and the target for the ExternalProject_Add() call
# to something that will highlight to the user what we are working on if
# something goes wrong and an error message is produced.

project(glog-populate NONE)



include(ExternalProject)
ExternalProject_Add(glog-populate
                     "UPDATE_DISCONNECTED" "False" "URL" "https://github.com/google/glog/archive/v0.4.0.zip" "URL_HASH" "MD5=2899b069b8229d49cd65eda5271315ad"
                    SOURCE_DIR          "/root/code/wetext_my/runtime/fc_base-GNU/glog-src"
                    BINARY_DIR          "/root/code/wetext_my/runtime/fc_base-GNU/glog-build"
                    CONFIGURE_COMMAND   ""
                    BUILD_COMMAND       ""
                    INSTALL_COMMAND     ""
                    TEST_COMMAND        ""
                    USES_TERMINAL_DOWNLOAD  YES
                    USES_TERMINAL_UPDATE    YES
)


