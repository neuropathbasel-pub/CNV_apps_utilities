import os
from pathlib import Path
from typing import Optional

class EnvironmentVariableNotFoundError(Exception):
    """Custom exception raised when a required environment variable is not found."""
    
    def __init__(self, variable_name: str, message: str = ""):
        self.variable_name = variable_name
        self.message = message or f"Environment variable '{variable_name}' not found."
        super().__init__(self.message)

def get_log_directory(env_variable: str):
    """
    Retrieve the log directory path from a specified environment variable.

    This function looks up an environment variable by name, checks if it's set,
    verifies if the path exists, and returns it as a `Path` object. If the 
    environment variable is not set, it defaults to the current directory (".").
    If the path specified by the environment variable does not exist, it raises 
    a `ValueError`.

    Args:
        env_variable (str): The name of the environment variable to look up for 
                            the log directory path.

    Returns:
        Path: A `Path` object representing the directory where logs should be 
              stored, either from the environment variable or the current directory.

    Raises:
        ValueError: If the environment variable is set but the path does not exist.

    Note:
        - This function does not create the directory if it doesn't exist; it only 
          checks for its existence.
        - The current directory is used as a fallback when the environment variable 
          is not set.
    """
    log_directory: Optional[str] = os.getenv(key=env_variable)

    if log_directory is None:
        log_directory = "."
    else:
        if not os.path.exists(path=log_directory):
            raise EnvironmentVariableNotFoundError(variable_name=env_variable)
    return Path(log_directory)

def get_path_from_env(env_variable: str, check_if_exists: bool = True) -> Path:
    """Retrieve a file path from an environment variable and validate it.
    Args:
        env_variable (str): The name of the environment variable to retrieve.
        logger: Logger object used to log error messages.
        check_if_exists (bool, optional): If True, checks if the path exists. Defaults to True.

    Returns:
        Path: A pathlib.Path object representing the validated file path.

    Raises:
        ValueError: If the environment variable is not set or if the path does not exist
            when check_if_exists is True.
    """
    env_value = os.getenv(env_variable)

    if env_value is None: 
        raise EnvironmentVariableNotFoundError(variable_name=env_variable)
    
    path = Path(env_value)
    if check_if_exists and not os.path.exists(path=env_value):
        raise EnvironmentVariableNotFoundError(variable_name=env_variable)
    
    return path

def get_integer_from_env(env_variable: str, default_value: int) -> int:
    """
    Retrieve an integer from an environment variable, with a fallback to a default value.

    This function attempts to fetch and convert an environment variable's value 
    to an integer. If the conversion fails due to the variable not being set or 
    containing non-integer data, it logs an error and returns the provided default 
    value.

    Args:
        env_variable (str): The name of the environment variable to look up.
        default_value (int, optional): The value to return if the environment 
                                       variable's value cannot be converted 
                                       to an integer.

    Returns:
        int: The integer value from the environment variable if conversion is 
             successful, otherwise the default_value.

    Note:
        - If the environment variable does not exist (i.e., `env_value` is `None`), 
          or if it cannot be converted to an integer, an error is logged but 
          no exception is raised; the default value is returned instead.
    """
    env_value: Optional[str] = os.getenv(key=env_variable)

    if env_value is None:
        print(f"Environment variable {env_variable} has not been found. Defaulting to {default_value}")
        return default_value
   
    try:
        return int(env_value)
    except ValueError:
        print(f"Error: {env_variable} environment variable '{env_variable}' is not a valid integer. Defaulting to {default_value}.")
        return default_value
    
def get_float_from_env(env_variable: str, default_value: float) -> float:
    """
    Retrieve a float value from an environment variable, with a default fallback.

    This function attempts to read and convert an environment variable to a float. If the 
    variable is not set or cannot be converted to a float, it logs an error and returns 
    the provided default value.

    Parameters:
    - env_variable (str): The name of the environment variable to look up.
    - default_value (float): The default float value to return if the environment variable 
                             is not set or not a valid float.

    Returns:
    - float: The float value from the environment variable, or the `default_value` if the 
             variable is not set or invalid.

    Raises:
    - No exceptions are raised; errors are logged instead.

    Notes:
    - This function uses `os.getenv` to check for the environment variable.
    - Errors are logged using a hypothetical `log_error` function which should be defined 
      elsewhere in the codebase for logging purposes.
    - The function does not modify the environment; it only reads from it.
    """
    
    env_value: Optional[str] = os.getenv(key=env_variable)

    if env_value is None:
        print(f"Error: {env_variable} environment variable has not been set in .env file. Defaulting to {default_value}.")
        return default_value
   
    try:
        return float(env_value)
    except ValueError:
        print(f"Error: {env_variable} environment variable '{env_variable}' is not a valid float. Defaulting to {default_value}.")
        return default_value
    
def get_string_from_env(env_variable: str, default_value: str = "", error_on_missing_value: bool = False) -> str:
    """
    Retrieve a string value from an environment variable.

    This function fetches the value of a specified environment variable and 
    returns it as a string. If the environment variable is not set, it raises 
    a `ValueError` with an informative message, logs the error, and prints it 
    to stdout.

    Args:
        value (str): The name of the environment variable to look up.


    Returns:
        str: The string value from the environment variable.
        - default_value (str): The default str value to return if the environment variable 
                             is not set or not a valid str.

    Raises:
        ValueError: If the environment variable is not set.

    Note:
        - This function assumes the existence of a `log_error` function for 
          logging error messages. Ensure this function is defined or imported.
        - The error message is both printed to stdout and logged for better 
          visibility and debugging.
    """

    env_value: Optional[str] = os.getenv(key=env_variable)

    if error_on_missing_value and env_value is None:
        raise EnvironmentVariableNotFoundError(variable_name=env_variable)

    try:
        return str(object=env_value)
    except ValueError:
        print(f"Error: {env_variable} environment variable '{env_variable}' is not a valid float. Defaulting to {default_value}.")
        return default_value

def get_boolean_from_env(env_variable: str, default_value: bool) -> bool:
    """
    Retrieve a boolean value from an environment variable.

    This function checks if the specified environment variable is set, attempts to convert its value to a boolean,
    and returns the boolean value or a default if conversion fails or the variable is not set.

    Args:
        env_variable (str): The name of the environment variable to check.
        default_value (bool): The value to return if the environment variable is not set or cannot be converted to a boolean.

    Returns:
        bool: The boolean value of the environment variable or the default value if conversion fails.

    Raises:
        Logs an error message if:
        - The environment variable is not set or
        - The value of the environment variable cannot be interpreted as a boolean.

    Note:
        - 'True' (case insensitive) will be interpreted as `True`, anything else as `False`.
        - This function uses `os.getenv` to fetch the environment variable, which returns `None` if the variable does not exist.
    """
    env_value: Optional[str] = os.getenv(key=env_variable)

    if env_value is None:
        print(f"Error: {env_variable} environment variable has not been set in .env file. Defaulting to {default_value}.")
        return default_value

    lower_env_value = env_value.lower()
    if lower_env_value in ('true', '1', 'yes', 'on'):
        return True
    elif lower_env_value in ('false', '0', 'no', 'off'):
        return False
    else:
        print(f"Error: {env_variable} environment variable '{env_value}' is not a valid boolean. Defaulting to {default_value}.")
        return default_value