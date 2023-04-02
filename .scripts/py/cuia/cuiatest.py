# Just testing the Cuia python framework
# Floatyboy - 32.03.2023
# Version 0.1
# License: GPL
# This is a test script for the Cuia python framework
# It is just a test script to see if the framework works
# It is not intended to be used in any way, shape or form
# It is just a test script

import asyncio
from dataclasses import dataclass
from cuia import Program, Store

@dataclass
class Hello(Store):
    x: int = 0
    y: int = 0

    def __str__(self):
        return f"\033[{self.x};{self.y}H\033[1mHello,world!"

program = Program(Hello(34, 12))

asyncio.run(program.start())

