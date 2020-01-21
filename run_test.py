
import lightcontrol
import labrobot
import time

robot = labrobot.robot('settings.json', 'waypoints.csv')
dmx_control = lightcontrol.dmx_control('output_light.txt', 0)
dmx_light_levels = [20, 30, 40]

for waypoint_name in robot.waypoints.index.values:
    print('Getting robot positioned')
    robot.move_to_waypoint(waypoint_name)
    for light_level in dmx_light_levels:
        print('Adjusting lights')
        dmx_control.dmx = light_level
        robot.wait_for_robot()
        dmx_control.wait_for_lights()
        print('Robot and lighting are set')
        print(f'DMX: {dmx_control.dmx}')
        print(f'Waypoint position: {waypoint_name}')
        print('Pausing for a few seconds pretending I am capturing data')
        time.sleep(3)

