import time
import math
import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("elf1_mini_biped.xml")
data = mujoco.MjData(model)

# Startpose laden
mujoco.mj_resetDataKeyframe(model, data, 0)
mujoco.mj_forward(model, data)

# Aktuator-IDs holen
left_pitch_id = mujoco.mj_name2id(
    model, mujoco.mjtObj.mjOBJ_ACTUATOR, "m_left_shoulder_pitch"
)
left_roll_id = mujoco.mj_name2id(
    model, mujoco.mjtObj.mjOBJ_ACTUATOR, "m_left_shoulder_roll"
)

print("left pitch:", left_pitch_id)
print("left roll :", left_roll_id)

with mujoco.viewer.launch_passive(model, data) as viewer:
    t = 0.0

    while viewer.is_running():
        data.ctrl[:] = 0.0

        # vor/zurück
        data.ctrl[left_pitch_id] = 0.25 * math.sin(3.0 * t)

        # seitlich, leicht phasenverschoben
        data.ctrl[left_roll_id] = 0.20 * math.sin(3.0 * t + 1.2)

        mujoco.mj_step(model, data)
        viewer.sync()

        t += model.opt.timestep
        time.sleep(model.opt.timestep)
