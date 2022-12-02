"""Constants for storing different classes of heros for the player to choose."""

heroes = {
    "Orc 1": {
        "position": (800, 500),
        "image_paths": ["orc.png"],
        "dimensions": (3 * 20, 3 * 32),
        "base_speed": 3,
        "health_points": 400,  # TODO: different classes can have different HPs and base attack forces
        "damage_image": "orc_dmg.png",
        "idle_image": "orc.png",
        "attack_image": "orc_atk.png",
    },
    "Orc 2": {
        "position": (800, 500),
        "image_paths": ["orc.png"],
        "dimensions": (3 * 20, 3 * 32),
        "base_speed": 3,
        "health_points": 400,  # TODO: different classes can have different HPs and base attack forces
        "damage_image": "orc_dmg.png",
        "idle_image": "orc.png",
        "attack_image": "orc_atk.png",
    },
}
