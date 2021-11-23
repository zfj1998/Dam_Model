import laspy
import numpy as np
import matplotlib as mpl
import ipdb


from_color = np.array(mpl.colors.to_rgb('blue'))
to_color = np.array(mpl.colors.to_rgb('red'))


def merge_color(value):
    return (1 - value)*from_color + value*to_color


def turn_value_into_rgb(array):
    '''
    input array: numpy array containing all the importance value
    '''
    min = np.min(array)
    shifted = array - min  # 从0开始
    max = np.max(shifted)
    normalized = shifted / max
    rgbs = np.array([merge_color(i) for i in normalized])*255
    return rgbs


def remove_white_space(array):
    result = []
    for i in array:
        if not i:
            continue
        result.append(i)
    return result


def read_dat():
    allx = []
    ally = []
    allz = []
    values = []
    intensity = []
    total_line = 142389
    line_count = 0
    with open('full.dat', 'r', encoding='utf8') as f:
        for line in f:
            line_count += 1
            if line_count < total_line/4:
                intensity.append(10)
            elif line_count < total_line/2:
                intensity.append(50)
            else:
                intensity.append(100)
            line_s = line.strip().split(' ')
            numbers = remove_white_space(line_s)
            allx.append(numbers[0])
            ally.append(numbers[1])
            allz.append(numbers[2])
            values.append(numbers[4])
    allx = np.array(allx, dtype='float32')
    ally = np.array(ally, dtype='float32')
    allz = np.array(allz, dtype='float32')
    values = np.array(values, dtype='float32')
    intensity = np.array(intensity, dtype='int')
    return allx, ally, allz, values, intensity


def main(out_file):
    hdr = laspy.header.Header(point_format=2)
    with laspy.file.File(out_file, mode="w", header=hdr) as lasfile:
        allx, ally, allz, values, intensity = read_dat()
        xmin = np.floor(np.min(allx))
        ymin = np.floor(np.min(ally))
        zmin = np.floor(np.min(allz))
        lasfile.header.offset = [xmin, ymin, zmin]
        lasfile.header.scale = np.array([0.001]*allx.shape[0])
        lasfile.x = allx
        lasfile.y = ally
        lasfile.z = allz
        lasfile.intensity = intensity
        allrgb = turn_value_into_rgb(values)

        lasfile.red = allrgb[:, 0]
        lasfile.green = allrgb[:, 1]
        lasfile.blue = allrgb[:, 2]


if __name__ == '__main__':
    out_file = 'full_intensity.las'
    main(out_file)
