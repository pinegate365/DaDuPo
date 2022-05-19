# Generated by https://quicktype.io
#
# To change quicktype's target language, run command:
#
#   "Set quicktype target language"
# from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from enum import Enum


@dataclass
class Alignment:
    alignment_byte: Optional[int]
    alignment_float32_ieee: Optional[int]
    alignment_float64_ieee: Optional[int]
    alignment_int64: Optional[int]
    alignment_long: Optional[int]
    alignment_word: Optional[int]

    def __init__(self, alignment_byte: Optional[int], alignment_float32_ieee: Optional[int],
                 alignment_float64_ieee: Optional[int], alignment_int64: Optional[int], alignment_long: Optional[int],
                 alignment_word: Optional[int]) -> None:
        self.alignment_byte = alignment_byte
        self.alignment_float32_ieee = alignment_float32_ieee
        self.alignment_float64_ieee = alignment_float64_ieee
        self.alignment_int64 = alignment_int64
        self.alignment_long = alignment_long
        self.alignment_word = alignment_word


class Datatype(Enum):
    A_INT64 = "A_INT64"
    A_UINT64 = "A_UINT64"
    FLOAT32_IEEE = "FLOAT32_IEEE"
    FLOAT64_IEEE = "FLOAT64_IEEE"
    SBYTE = "SBYTE"
    SLONG = "SLONG"
    SWORD = "SWORD"
    UBYTE = "UBYTE"
    ULONG = "ULONG"
    UWORD = "UWORD"


class ParameterType(Enum):
    ARRAY = "ARRAY"
    ASCII = "ASCII"
    CURVE = "CURVE"
    MAP = "MAP"
    VALUE = "VALUE"


class ByteOrder(Enum):
    MSB_FIRST = "MSB_FIRST"
    MSB_LAST = "MSB_LAST"


@dataclass
class Coeffs:
    a: float
    b: float

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b


class CompuMethodType(Enum):
    DICT = "DICT"
    LINEAR = "LINEAR"
    IDENTICAL = "IDENTICAL"


@dataclass
class CompuMethod:
    coeffs: Optional[Coeffs]
    compu_method_type: CompuMethodType
    dictionary: Optional[Dict[str, Any]]  # key shall be integer string: "1"
    name: str
    unit: Optional[str]

    def __init__(self, coeffs: Optional[Coeffs], compu_method_type: CompuMethodType,
                 dictionary: Optional[Dict[str, Any]], name: str, unit: Optional[str]) -> None:
        self.coeffs = coeffs
        self.compu_method_type = compu_method_type
        self.dictionary = dictionary
        self.name = name
        self.unit = unit


@dataclass
class Asap2Parameter:
    address: str
    alignment: Optional[Alignment]
    compu_method: Optional[str]
    count: int
    datatype: Datatype
    description: Optional[str]
    identifier: Optional[str]
    name: str
    parameter_type: ParameterType
    ref_x: Optional[str]
    ref_y: Optional[str]
    unit: Optional[str]
    db_desc: Optional[str]
    bitmask: Optional[str]

    def __init__(self, address: str, alignment: Optional[Alignment], compu_method: Optional[str], count: int,
                 datatype: Datatype, description: Optional[str], identifier: Optional[str], name: str,
                 parameter_type: ParameterType, ref_x: Optional[str], ref_y: Optional[str],
                 unit: Optional[str], db_desc: Optional[str], bitmask: Optional[str]) -> None:
        self.address = address
        self.alignment = alignment
        self.compu_method = compu_method
        self.count = count
        self.datatype = datatype
        self.description = description
        self.identifier = identifier
        self.name = name
        self.parameter_type = parameter_type
        self.ref_x = ref_x
        self.ref_y = ref_y
        self.unit = unit
        self.db_desc = db_desc
        self.bitmask = bitmask


@dataclass
class Asap2Signal:
    address: str
    alignment: Optional[Alignment]
    compu_method: Optional[str]
    count: Optional[int]
    datatype: Datatype
    description: Optional[str]
    identifier: Optional[str]
    name: str
    unit: Optional[str]
    db_desc: Optional[str]
    bitmask: Optional[str]

    def __init__(self, address: str, alignment: Optional[Alignment], compu_method: Optional[str], count: Optional[int],
                 datatype: Datatype, description: Optional[str], identifier: Optional[str], name: str,
                 unit: Optional[str], db_desc: Optional[str], bitmask: Optional[str]) -> None:
        self.address = address
        self.alignment = alignment
        self.compu_method = compu_method
        self.count = count
        self.datatype = datatype
        self.description = description
        self.identifier = identifier
        self.name = name
        self.unit = unit
        self.db_desc = db_desc
        self.bitmask = bitmask


class DBType(Enum):
    ASAP2 = "ASAP2"


@dataclass
class Asap2Database:
    """Asap2 database of DaDuPo"""
    alignment: Optional[Alignment]
    asap2_parameters: List[Asap2Parameter]
    asap2_signals: List[Asap2Signal]
    byte_order: ByteOrder
    compu_methods: List[CompuMethod]
    db_type: DBType
    db_desc: Optional[str]
    name: str

    def __init__(self, alignment: Optional[Alignment], asap2_parameters: List[Asap2Parameter],
                 asap2_signals: List[Asap2Signal], byte_order: ByteOrder, compu_methods: List[CompuMethod],
                 db_type: DBType, db_desc: Optional[str], name: str) -> None:
        self.alignment = alignment
        self.asap2_parameters = asap2_parameters
        self.asap2_signals = asap2_signals
        self.byte_order = byte_order
        self.compu_methods = compu_methods
        self.db_type = db_type
        self.db_desc = db_desc
        self.name = name
