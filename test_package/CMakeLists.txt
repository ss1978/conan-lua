project(luatest)

find_package(lua)

enable_testing()
include(CTest)
add_executable(${PROJECT_NAME} test.c)
include_directories(${lua_INCLUDES})
target_link_libraries(${PROJECT_NAME} ${lua_LIBS} m)
add_test(${PROJECT_NAME} ${PROJECT_BINARY_DIR}/${PROJECT_NAME})