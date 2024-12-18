import pathlib
import os
from hashlib import md5
from time import perf_counter
from config import settings


def get_hashsum(settings_path: str) -> str:
    """Get hashsum of settings file."""
    with open(settings_path, 'rb') as file:
        return md5(file.read()).hexdigest()


if __name__ == '__main__':
    # Get current hashsum to check for settings updates
    HERE = pathlib.Path(__file__).parent.resolve()
    settings_path = os.path.join(HERE, 'settings.toml')
    current_hashsum = get_hashsum(settings_path)

    start_program = perf_counter()
    end = perf_counter()

    process_times = []
    print('Beginning timing...')
    while (end-start_program) < 10:
        start_loop = perf_counter()

        # Check if settings has updated
        new_hashsum = get_hashsum(settings_path)
        if new_hashsum != current_hashsum:
            # Settings has updated
            settings.configure()

        # Read values
        first = settings.first.value
        second = settings.second.value
        third = settings.third.value

        # Calculate process time
        end = perf_counter()
        process_time_ms = (end-start_loop) * 1000
        process_times.append(process_time_ms)

    # Print results
    average_process_time = sum(process_times) / len(process_times)
    print('Finished.')
    print('Average process time (ms):', average_process_time)
