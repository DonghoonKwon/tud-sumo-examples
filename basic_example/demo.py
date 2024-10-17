from tud_sumo.simulation import Simulation

if __name__ == "__main__":

    # Initialise the simulation object.
    my_sim = Simulation(scenario_name="basic_scenario",
                        scenario_desc="TUD-SUMO integrity check.")

    # Start the simulation, defining the sumo config files.
    my_sim.start("basic_scenario/sumo_config.sumocfg",
                 gui=True,
                 seed=1)
    
    # Run through the simulation for 1000 steps.
    my_sim.step_through(n_steps=1000)

    # End the simulation.
    my_sim.end()

    # Save the simulation data & print a summary, which is also saved.
    my_sim.save_data("example_data.json")
    my_sim.print_summary(save_file="example_summary.txt")
    