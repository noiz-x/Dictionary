# Dictionary

Dictionary is a Python program that allows you to interact with a dictionary stored in a JSON file. You can perform operations such as looking up terms, adding new terms, redefining terms, deleting terms, and searching for terms based on a phrase.

## Prerequisites

- Python 3.x
- JSON library (comes with Python)

## Requirements

- pyautogui==0.9.53

## Usage

1. Clone or download the repository to your local machine.

2. Ensure that the `dictionary.json` file is in the same directory as the `dictionary.py` file. This file will store the dictionary data.

3. Open a terminal or command prompt and navigate to the directory containing the `dictionary.py` file.

4. Run the program using the following command:

   ```shell
   pip install -r requirements.txt
   python dictionary.py
   ```

5. Once the program starts, you will see a menu with different options:

   - **0**: Quit the program.
   - **1**: Lookup a term.
   - **2**: Add a term.
   - **3**: Redefine a term.
   - **4**: Delete a term.
   - **5**: Search for a term based on a phrase.
   - **`**: Print all dictionary keys.
   - **~**: Print all dictionary items.

6. Choose an option by entering the corresponding number or character and pressing Enter. Follow the prompts to perform the desired operation.

7. To exit the program, choose option **0** or enter **q** when prompted for a choice.

## Customization

You can modify the `dictionary.json` file to pre-populate the dictionary with your own terms and definitions. The file should be in the following format:

```json
{
  "Term 1": "Definition 1",
  "Term 2": "Definition 2",
  ...
}
```

Feel free to add, remove, or modify the terms and definitions as needed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
