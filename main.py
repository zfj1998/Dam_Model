
import ipdb
import numpy as np

from util import read_dat, write_las, build_paths, value_into_rgb


def handle_section(section_dat_paths, other_paths, las_path):
    '''
    制作某断面展示模型
    '''
    section_positions, _ = read_dat(section_dat_paths[0])
    for section_dat_path in section_dat_paths[1:]:
        positions, _ = read_dat(section_dat_path)
        section_positions = np.concatenate((section_positions, positions))
    other_positions, _ = read_dat(other_paths[0])
    for dat_path in other_paths[1:]:
        positions, _ = read_dat(dat_path)
        other_positions = np.concatenate((other_positions, positions))
    rgb = np.ones((section_positions.shape[0] + other_positions.shape[0], 3))*255
    section_intensity = np.ones(section_positions.shape[0])*1500
    other_intensity = np.ones(other_positions.shape[0])*10
    position = np.concatenate((section_positions, other_positions))
    intensity = np.concatenate((section_intensity, other_intensity))
    write_las(las_path, position, intensity, rgb)


def handle_5_section(las_path):
    sections = []
    base_dir = './data/dc3dc4dc5'
    section_dat_paths = build_paths(base_dir, [
        '1-1断面.dat',
        '2-2断面.dat',
        '3-3断面.dat',
        '4-4断面.dat',
        '5-5断面.dat'
    ])
    other_paths = build_paths(base_dir, [
        'others.dat'
    ])
    


def handle_points(point_paths, section_dat_paths, other_paths, las_path):
    '''
    制作某断面某测点群展示模型
    '''
    point_positions, _ = read_dat(point_paths[0])
    for point_path in point_paths[1:]:
        positions, _ = read_dat(point_path)
        point_positions = np.concatenate((point_positions, positions))
    section_positions, _ = read_dat(section_dat_paths[0])
    for section_dat_path in section_dat_paths[1:]:
        positions, _ = read_dat(section_dat_path)
        section_positions = np.concatenate((section_positions, positions))
    other_positions, _ = read_dat(other_paths[0])
    for dat_path in other_paths[1:]:
        positions, _ = read_dat(dat_path)
        other_positions = np.concatenate((other_positions, positions))
    red = value_into_rgb(np.ones(point_positions.shape[0]))
    white = np.ones((section_positions.shape[0] + other_positions.shape[0], 3))*255
    point_intensity = np.ones(point_positions.shape[0])*1500
    section_intensity = np.ones(section_positions.shape[0])*100
    other_intensity = np.ones(other_positions.shape[0])*10
    position = np.concatenate((point_positions, section_positions, other_positions))
    intensity = np.concatenate((point_intensity, section_intensity, other_intensity))
    rgb = np.concatenate((red, white))
    write_las(las_path, position, intensity, rgb)



def handle_force():
    '''
    制作彩色数值分析模型
    '''
    pass


if __name__ == '__main__':
    # base_dir = './data/dc3dc4dc5'
    # las_path = './out/5-5断面.las'
    # section_dat_paths = build_paths(base_dir, [
    #     '5-5断面.dat'
    # ])
    # other_paths = build_paths(base_dir, [
    #     '1-1断面.dat',
    #     '3-3断面dc3测点.dat',
    #     '3-3断面dc4测点.dat',
    #     '3-3断面dc5测点.dat',
    #     '3-3断面其他.dat',
    #     '2-2断面.dat',
    #     '4-4断面.dat',
    #     'others.dat',
    # ])
    # handle_section(section_dat_paths, other_paths, las_path)

    base_dir = './data/dc3dc4dc5'
    las_path = './out/3-3断面dc4测点.las'
    point_dat_paths = build_paths(base_dir, [
        '3-3断面dc4测点.dat',
    ])
    section_dat_paths = build_paths(base_dir, [
        '3-3断面dc3测点.dat',
        '3-3断面dc5测点.dat',
        '3-3断面其他.dat',
    ])
    other_paths = build_paths(base_dir, [
        '1-1断面.dat',
        '2-2断面.dat',
        '4-4断面.dat',
        '5-5断面.dat',
        'others.dat',
    ])
    handle_points(point_dat_paths, section_dat_paths, other_paths, las_path)
