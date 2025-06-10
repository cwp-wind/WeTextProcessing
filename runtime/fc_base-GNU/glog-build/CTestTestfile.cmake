# CMake generated Testfile for 
# Source directory: /root/code/wetext_my/runtime/fc_base-GNU/glog-src
# Build directory: /root/code/wetext_my/runtime/fc_base-GNU/glog-build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(demangle "/root/code/wetext_my/runtime/fc_base-GNU/glog-build/demangle_unittest")
set_tests_properties(demangle PROPERTIES  _BACKTRACE_TRIPLES "/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;626;add_test;/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;0;")
add_test(logging "/root/code/wetext_my/runtime/fc_base-GNU/glog-build/logging_unittest")
set_tests_properties(logging PROPERTIES  _BACKTRACE_TRIPLES "/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;627;add_test;/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;0;")
add_test(signalhandler "/root/code/wetext_my/runtime/fc_base-GNU/glog-build/signalhandler_unittest")
set_tests_properties(signalhandler PROPERTIES  _BACKTRACE_TRIPLES "/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;630;add_test;/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;0;")
add_test(stacktrace "/root/code/wetext_my/runtime/fc_base-GNU/glog-build/stacktrace_unittest")
set_tests_properties(stacktrace PROPERTIES  TIMEOUT "30" _BACKTRACE_TRIPLES "/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;634;add_test;/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;0;")
add_test(stl_logging "/root/code/wetext_my/runtime/fc_base-GNU/glog-build/stl_logging_unittest")
set_tests_properties(stl_logging PROPERTIES  _BACKTRACE_TRIPLES "/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;638;add_test;/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;0;")
add_test(symbolize "/root/code/wetext_my/runtime/fc_base-GNU/glog-build/symbolize_unittest")
set_tests_properties(symbolize PROPERTIES  _BACKTRACE_TRIPLES "/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;641;add_test;/root/code/wetext_my/runtime/fc_base-GNU/glog-src/CMakeLists.txt;0;")
