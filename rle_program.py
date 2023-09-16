from console_gfx import ConsoleGfx

def to_hex_string(data):
    # take a list of data (integers)
    # convert to hex characters (string)
    # concatenate string
    hex_string = ''
    for char in data:
        if char == 10:
            char = 'a'
        if char == 11:
            char = 'b'
        if char == 12:
            char = 'c'
        if char == 13:
            char = 'd'
        if char == 14:
            char = 'e'
        if char == 15:
            char = 'f'
        else:
            char
        hex_string += str(char)
    return hex_string


def count_runs(flat_data):
    current = flat_data[0]
    num_count = 1
    run_count = 1
    for num in flat_data[1:]:
        if current == num:
            num_count += 1
            if num_count > 15:
                run_count += 1
                num_count = 1
            continue
        else:
            current = num
            run_count += 1
    return run_count

def encode_rle(flat_data):
    current = flat_data[0]
    list = []
    count = 1
    for num in flat_data[1:]:
        if current == num:
            count += 1
            if count > 15:
                list.extend([count - 1, current])
                current = num
                count = 1
        else:
            list.extend([count, current])
            count = 1
            current = num
    list.extend([count, num])
    return list

def get_decoded_length(rle_data):
    data = rle_data[0:-1:2]
    res = 0
    for i in data:
        res += int(i)
    return res

def decode_rle(rle_data):
    res = []
    for idx in range(0, len(rle_data), 2):
        value = rle_data[idx + 1]
        repeated_times = int(rle_data[idx])
        res.extend([value] * repeated_times)
    return res


def string_to_data(data_string):
    # take in a string
    # change to list
    # translate characters to integers
    data_list = []
    for i in data_string:
        data_list.append(i)
    for i in range(0, len(data_list)):
        if data_list[i] == 'a':
            data_list[i] = 10
        elif data_list[i] == 'b':
            data_list[i] = 11
        elif data_list[i] == 'c':
            data_list[i] = 12
        elif data_list[i] == 'd':
            data_list[i] = 13
        elif data_list[i] == 'e':
            data_list[i] = 14
        elif data_list[i] == 'f':
            data_list[i] = 15
        else:
            data_list[i] = int(data_list[i])
    return data_list

def to_rle_string(rle_data):
    for i in range(1, len(rle_data) + 1, 2):
        if rle_data[i] == 10:
            rle_data[i] = 'a'
        if rle_data[i] == 11:
            rle_data[i] = 'b'
        if rle_data[i] == 12:
            rle_data[i] = 'c'
        if rle_data[i] == 13:
            rle_data[i] = 'd'
        if rle_data[i] == 14:
            rle_data[i] = 'e'
        if rle_data[i] == 15:
            rle_data[i] = 'f'
        else:
            rle_data[i] = str(rle_data[i])
    for i in range(0, len(rle_data), 2):
        rle_data[i] = str(rle_data[i])
    rle_string = []
    rle_string_2 = []
    for i in range(0, len(rle_data), 2):
        rle_element = rle_data[i] + rle_data[i + 1]
        rle_string.append(rle_element)
    for i in range(0, len(rle_string) - 1):
        rle_string[i] = rle_string[i] + ":"
        rle_string_2.append(rle_string[i])
    rle_str = ""
    for i in rle_string:
        rle_str += i
    return rle_str



def string_to_rle(rle_string):
    rle_list = rle_string.split(":")
    rle_list_2 = []
    for i in rle_list:
        if len(i) == 3:
            a = i[0:2]
            b = i[2]
            if b == 'a' or b == 'A':
                b = 10
            elif b == 'b' or b == 'B':
                b = 11
            elif b == 'c' or b == 'C':
                b = 12
            elif b == 'd' or b == 'D':
                b = 13
            elif b == 'e' or b == "E":
                b = 14
            elif b == 'f' or b == 'F':
                b = 15
            else:
                b = int(b)
            element = (int(a), b)
            rle_list_2.extend(element)
        elif len(i) == 2:
            a = i[0]
            b = i[1]
            if b == 'a' or b == 'A':
                b = 10
            elif b == 'b' or b == 'B':
                b = 11
            elif b == 'c' or b == 'C':
                b = 12
            elif b == 'd' or b == 'D':
                b = 13
            elif b == 'e' or b == "E":
                b = 14
            elif b == 'f' or b == 'F':
                b = 15
            else:
                b = int(b)
            element = (int(a), b)
            rle_list_2.extend(element)
    return rle_list_2



if __name__ == '__main__':

    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")

    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    image_data = None

    while True:
        print("\nRLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String"
              "\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n"
              "8. Display Hex RLE Data\n9. Display Hex Flat Data\n")
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            filename = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(filename)
        elif option == 2:
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.")
        elif option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            rle_list_2 = string_to_rle(rle_string)
            flat_byte = decode_rle(rle_list_2)
        elif option == 4:
            hex_string = input("Enter the hex string holding RLE data: ")
            data_list = string_to_data(hex_string)
            flat_byte = decode_rle(data_list)
        elif option == 5:
            flat_data_hex = input("Enter the hex string holding flat data: ")
            flat_byte = decode_rle(flat_data_hex)
        elif option == 6:
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)
        elif option == 7:
            print("RLE representation:", end=" ")
            list = encode_rle(flat_byte)
            print(to_rle_string(list))
        elif option == 8:
            print("RLE hex values:", end=" ")
            list = encode_rle(flat_byte)
            print(to_hex_string(list))
        elif option == 9:
            print("Flat hex values:", end=" ")
            print(to_hex_string(flat_byte))
        else:
            print("Error! Invalid input.")