import os
from os import path

curDir = os.getcwd()
PROJECT = path.join(curDir, 'Debug', 'build')

prefix = 'arm-none-eabi-'

CC = prefix + 'gcc'
CXX = prefix + 'g++'
AR = prefix + 'ar'
LINK = prefix + 'gcc'
AS = prefix + 'gcc -x assembler-with-cpp'
OBJCOPY = prefix + 'objcopy'
OBJDUMP = prefix + 'objdump'
SIZE = prefix + 'size'

CPU = '-mcpu=cortex-m0'
FPU_FLAGS = '' #'-mfloat-abi=hard -mfpu=fpv4-sp-d16'
#FPU_FLAGS = '-mfloat-abi=soft'
MPU = CPU + ' -mthumb ' + FPU_FLAGS + ' -mthumb -mthumb-interwork -ffunction-sections -fdata-sections \
    -g -fno-common -fmessage-length=0 -specs=nosys.specs -specs=nano.specs'

CPPDEFINES = ['-DUSE_HAL_DRIVER',
              '-DARM_MATH_CM0']

ASFLAGS = MPU
CXXFLAGS = MPU + ' std=c++11'
CCFLAGS = MPU + ' -std=gnu99'
LDFLAGS = '-Wl,-gc-sections,--print-memory-usage -T linkscripts/link.lds' + ' -Wl,-Map=' + PROJECT +'.map'

CPPPATH = ['-Iapplications']
         
TARGET = PROJECT + '.elf'
HEX_TARGET = PROJECT + '.hex'
BIN_TARGET = PROJECT + '.bin'
