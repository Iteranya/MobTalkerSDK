from dataclasses import dataclass
from enum import Enum
# Feel free to expand these base classes~

class Character:
    def __init__(self, id=None, name=None, description=None, thoughts=None):
        self._id = id
        self._name = name
        self._description = description
        self._thoughts = thoughts
        self._outfit = f"<{id}_outfit>"
        self._states = f"<{id}_state>"
        self._maxhealth = f"<{id}_maxhealth>"
        self._health = f"<{id}_health>"
        self._hostile = f"<{id}_hostile>"
        self._traits = f"<{id}_traits>"
        self._mob_type = f"<{id}_mob_type"
        self._mood = f"<{id}_mood>"

    # Getter and Setter for id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # Getter and Setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Getter and Setter for description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    # Getter and Setter for thoughts
    @property
    def thoughts(self):
        return self._thoughts

    @thoughts.setter
    def thoughts(self, value):
        self._thoughts = value

    # Getter and Setter for outfit
    @property
    def outfit(self):
        return self._outfit

    @outfit.setter
    def outfit(self, value):
        self._outfit = value

    # Getter and Setter for states
    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, value):
        self._states = value

    # Getter and Setter for maxhealth
    @property
    def maxhealth(self):
        return self._maxhealth

    @maxhealth.setter
    def maxhealth(self, value):
        self._maxhealth = value

    # Getter and Setter for traits
    @property
    def traits(self):
        return self._traits

    @traits.setter
    def traits(self, value):
        self._traits = value

    # Getter and Setter for mob_type
    @property
    def mob_type(self):
        return self._mob_type

    @mob_type.setter
    def mob_type(self, value):
        self._mob_type = value

        # Getter and Setter for mood
    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, value):
        self._mood = value

class Status():
    IS_DAY = "<is_day>"
    HOSTILES = "<hostiles>"
    BELOW_SKY = "<below_sky>"
    NEAR_HOME = "<near_home>"
    P_UID = "<p_uid>"
    P_HEALTH = "<p_health>"
    GAMEMODE = "<gamemode>"
    DIMENSION = "<dimension>"
    X_COOR = "<x_coor>"
    Y_COOR = "<y_coor>"
    Z_COOR = "<z_coor>"
    HELD_ITEM = "<held_item>"
    