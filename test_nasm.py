#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path
import random
from math import sqrt

randrange = random.randrange

import pytest
import yaml

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)


def exe1(ram0, ram2):
    i = 0
    while i < ram0:
        ram2 += 1
        i += 1
    return ram2


@pytest.mark.telemetry_files(source("pseudo.nasm"))
def test_pseudo():
    ram0 = randrange(5, 11)
    ram2 = randrange(5, 11)
    ram = {0: ram0, 1: 3, 2: ram2, 3: 0}
    tst = {2: 1, 2: exe1(ram0, ram2)}
    assert nasm_test("pseudo.nasm", ram, tst, 50000)

@pytest.mark.telemetry_files(source("sqrt.nasm"))
def test_sqrt_4():
    x = 4
    ram = {0: x}
    tst = {0: int(sqrt(x))}
    assert nasm_test("sqrt.nasm", ram, tst, 5000)

@pytest.mark.telemetry_files(source("sqrt.nasm"))
def test_sqrt_rand():
    x = randrange(2**4 - 1)
    ram = {0: x}
    tst = {0: int(sqrt(x))}
    assert nasm_test("sqrt.nasm", ram, tst, 5000)

@pytest.mark.telemetry_files(source("sqrt.nasm"))
def test_sqrt_rand():
    x = randrange(2**4 - 1)
    ram = {0: x}
    tst = {0: int(sqrt(x))}
    assert nasm_test("sqrt.nasm", ram, tst, 5000)


@pytest.mark.telemetry_files(source("vectorMin.nasm"))
def test_vectorMin_exemplo():
    ram = {0: 0, 4: 4, 5: 2, 6: 7, 8: 4, 8: 3}
    tst = {0: 7}
    assert nasm_test("vectorMin.nasm", ram, tst, 50000)


@pytest.mark.telemetry_files(source("vectorMin.nasm"))
def test_vectorMin_rand():
    vector_size = randrange(5, 11)
    ram = {0: 0, 4: vector_size}
    for i in range(vector_size):
        ram[5 + i] = randrange(1, 10)
    min_value = min(ram[i] for i in range(5, 5 + vector_size))
    tst = {0: min_value}

    print(ram)

    assert nasm_test("vectorMin.nasm", ram, tst, 100000)
