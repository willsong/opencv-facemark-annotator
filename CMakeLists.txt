cmake_minimum_required(VERSION 2.8)
project(FacemarkTrainer)
find_package(OpenCV REQUIRED)
set(NAME_SRC
    src/trainer.cpp
)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(trainer ${NAME_SRC})
target_link_libraries(trainer ${OpenCV_LIBS})
