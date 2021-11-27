
import ipdb
import numpy as np

from util import read_dat, write_las, build_paths, value_into_rgb, build_points

base_dir = './data'

def outter_points():
    section_dat_paths = build_paths(base_dir, [
        '坝顶.dat',
        '底部.dat',
        '上下游面.dat',
    ])
    return build_points(section_dat_paths, 101, 'white')

def other_points(exclusive):
    all_data_paths = build_paths(base_dir, [
        'NALL.dat',
    ])
    return build_points(all_data_paths, 103, 'white', exclusive)


def basic_model():
    '''
    基本模型展示
    '''
    las_path = './out/基本模型.las'
    sec_pos, sec_int, sec_col = outter_points()

    heart_dat_paths = build_paths(base_dir, [
        '心墙.dat',
    ])
    ht_pos, ht_int, ht_col = build_points(heart_dat_paths, 102, 'white')
    
    other_than_all_pos = np.concatenate((sec_pos, ht_pos))
    other_pos, other_int, other_col = other_points(other_than_all_pos)

    position = np.concatenate((sec_pos, ht_pos, other_pos))
    intensity = np.concatenate((sec_int, ht_int, other_int))
    rgb = np.concatenate((sec_col, ht_col, other_col))
    write_las(las_path, position, intensity, rgb)

def five_sections():
    '''
    绘制五个截面
    '''
    las_path = './out/五个断面.las'
    base_dir = './data'
    outter_pos, outter_int, outter_col = outter_points()

    section1_paths = build_paths(base_dir, ['断面1-1.dat'])
    sec1_pos, sec1_int, sec1_col = build_points(section1_paths, 104, 'white')
    section2_paths = build_paths(base_dir, ['断面2-2.dat'])
    sec2_pos, sec2_int, sec2_col = build_points(section2_paths, 105, 'white')
    section3_paths = build_paths(base_dir, ['断面3-3.dat'])
    sec3_pos, sec3_int, sec3_col = build_points(section3_paths, 106, 'white')
    section4_paths = build_paths(base_dir, ['断面4-4.dat'])
    sec4_pos, sec4_int, sec4_col = build_points(section4_paths, 107, 'white')
    section5_paths = build_paths(base_dir, ['断面5-5.dat'])
    sec5_pos, sec5_int, sec5_col = build_points(section5_paths, 108, 'white')

    other_than_all_pos = np.concatenate((outter_pos, sec1_pos, sec2_pos, sec3_pos, sec4_pos, sec5_pos))
    other_pos, other_int, other_col = other_points(other_than_all_pos)

    position = np.concatenate((outter_pos, sec1_pos, sec2_pos, sec3_pos, sec4_pos, sec5_pos, other_pos))
    intensity = np.concatenate((outter_int, sec1_int, sec2_int, sec3_int, sec4_int, sec5_int, other_int))
    rgb = np.concatenate((outter_col, sec1_col, sec2_col, sec3_col, sec4_col, sec5_col, other_col))
    write_las(las_path, position, intensity, rgb)


def handle_force():
    '''
    制作彩色数值分析模型
    '''
    pass


if __name__ == '__main__':
    basic_model()
