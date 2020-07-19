# define the correct path and name
export PATH 		:= c:/raylib/mingw/bin:$(PATH)
PROJECT_NAME        ?= GAMENAME
OUTDIR				= bin/
SOURCE				= src/
DEBUGGING           ?= TRUE

CC = g++
MAKE = mingw32-make

ifeq ($(DEBUGGING), TRUE)
	CFLAGS += -g
else
	CFLAGS += -O1 -s
endif

CFLAGS += -Wall -D_DEFAULT_SOURCE -Wno-missing-braces
# CFLAGS += -Wl,--subsystem,windows

INCLUDE_PATHS = -I.
LDFLAGS = -L.
LDLIBS = -lraylib -lgdi32 -lwinmm -static

PROJECT_SOURCE_FILES ?= $(wildcard $(SOURCE)*.cpp $(SOURCE)**/*.cpp)
OBJS = $(patsubst %.cpp, %.o, $(PROJECT_SOURCE_FILES))

.PHONY: all

all:
	$(MAKE) $(PROJECT_NAME)
	$(OUTDIR)$(PROJECT_NAME)

$(PROJECT_NAME): $(OBJS)
	$(CC) -o $(OUTDIR)$(PROJECT_NAME)$(EXT) $(OBJS) $(CFLAGS) $(INCLUDE_PATHS) $(LDFLAGS) $(LDLIBS)

clean:
	del $(wildcard $(SOURCE)*.o $(SOURCE)**/*.o)
