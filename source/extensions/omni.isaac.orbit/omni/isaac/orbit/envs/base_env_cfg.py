# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES, ETH Zurich, and University of Toronto
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Base configuration of the environment.

This module defines the general configuration of the environment. It includes parameters for
configuring the environment instances, viewer settings, and simulation parameters.
"""

from dataclasses import MISSING
from typing import Tuple

from omni.isaac.orbit.command_generators import CommandGeneratorBaseCfg
from omni.isaac.orbit.scene import InteractiveSceneCfg
from omni.isaac.orbit.sim import SimulationCfg
from omni.isaac.orbit.utils import configclass

__all__ = ["BaseEnvCfg", "ViewerCfg"]


@configclass
class ViewerCfg:
    """Configuration of the scene viewport camera."""

    eye: Tuple[float, float, float] = (7.5, 7.5, 7.5)
    """Initial camera position (in m). Default is (7.5, 7.5, 7.5)."""
    lookat: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    """Initial camera target position (in m). Default is (0.0, 0.0, 0.0)."""
    resolution: Tuple[int, int] = (1280, 720)
    """The resolution (width, height) of the default viewport (in pixels). Default is (1280, 720).

    This is the resolution of the camera "/OmniverseKit_Persp", that is used in default viewport.
    The camera is also used for rendering RGB images of the simulation.
    """


@configclass
class BaseEnvCfg:
    """Base configuration of the environment."""

    # simulation settings
    viewer: ViewerCfg = ViewerCfg()
    """Viewer configuration. Default is ViewerCfg()."""
    sim: SimulationCfg = SimulationCfg()
    """Physics simulation configuration. Default is SimulationCfg()."""

    # general settings
    decimation: int = MISSING
    """Number of control action updates @ sim dt per policy dt."""

    # environment settings
    scene: InteractiveSceneCfg = MISSING
    """Scene settings"""
    observations: object = MISSING
    """Observation space settings."""
    actions: object = MISSING
    """Action space settings."""
    commands: CommandGeneratorBaseCfg = MISSING
    """Command generator settings."""