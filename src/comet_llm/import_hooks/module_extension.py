# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at https://www.comet.com
#  Copyright (C) 2015-2023 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************

from typing import Dict

from . import callable_extenders


class ModuleExtension:
    def __init__(self) -> None:
        self._callables_extenders: Dict[str, callable_extenders.CallableExtenders] = {}

    def extenders(self, callable_name: str) -> callable_extenders.CallableExtenders:
        if callable_name not in self._callables_extenders:
            self._callables_extenders[callable_name] = callable_extenders.get()

        return self._callables_extenders[callable_name]

    def items(self):  # type: ignore
        return self._callables_extenders.items()
