import laspy
import numpy as np
import matplotlib as mpl


from_color = np.array(mpl.colors.to_rgb('blue'))
to_color = np.array(mpl.colors.to_rgb('red'))


def build_paths(base_dir, files):
    result = []
    for file_name in files:
        result.append(f'{base_dir}/{file_name}')
    return result


def merge_color(value):
    return (1 - value)*from_color + value*to_color


def normalize(array):
    '''
    input array: numpy array containing all the importance value
    '''
    min = np.min(array)
    shifted = array - min  # 从0开始
    max = np.max(shifted)
    normalized = shifted / max
    return normalized


def value_into_rgb(array):
    '''
    input array: numpy array range from 0 to 1
    '''
    rgbs = np.array([merge_color(i) for i in array])*255
    return rgbs


def write_las(file_path, position, intensity, rgb):
    '''
    file_path: str, the path to the target las file
    position: contains tuples like (x, y, z), which are numpy arrays for points' positions
    intensity: integer values, control the transparency of points
    rgb: contains tuples like (red, green, blue), values ranges from 0~255
    '''
    hdr = laspy.header.Header(point_format=2)  # lasfile type 2 is with RGB
    with laspy.file.File(file_path, mode="w", header=hdr) as lasfile:
        x, y, z = position[:, 0], position[:, 1], position[:, 2]
        xmin = np.floor(np.min(x))
        ymin = np.floor(np.min(y))
        zmin = np.floor(np.min(z))
        lasfile.header.offset = [xmin, ymin, zmin]
        lasfile.header.scale = np.array([0.001]*x.shape[0])
        lasfile.x = x
        lasfile.y = y
        lasfile.z = z
        lasfile.intensity = intensity
        lasfile.red = rgb[:, 0]
        lasfile.green = rgb[:, 1]
        lasfile.blue = rgb[:, 2]


def remove_white_space(array):
    result = []
    for i in array:
        if not i:
            continue
        result.append(i)
    if len(result) != 6:
        return None
    return result


def read_dat(file_path, value_index=3):
    '''
    value_index: the columns index of values that are needed
    '''
    positions = []
    values = []
    lc = 0
    with open(file_path, 'r', encoding='utf8') as f:
        for line in f:
            lc += 1
            line_s = line.strip().split('\t')
            numbers = remove_white_space(line_s)
            if not numbers:
                print(f'Warning: jump {file_path} line {lc}')
                continue
            positions.append([numbers[0], numbers[1], numbers[2]])
            values.append(numbers[value_index])
    positions = np.array(positions, dtype='float32')
    values = np.array(values, dtype='float32')
    return positions, values
