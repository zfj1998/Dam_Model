
import ipdb
import numpy as np

from util import read_dat, write_las, build_paths, value_into_rgb, build_points

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

def outter_points():
    section_dat_paths = build_paths(base_dir, [
        'badi.dat',
        'badng.dat',
    ])
    return build_points(section_dat_paths, 101, 'white')

def other_points(exclusive):
    all_data_paths = build_paths(base_dir, [
        'NALL-Z.dat',
    ])
    return build_points(all_data_paths, 107, 'white', exclusive)

def main():
    # 外壳
    outter_pos, outter_int, outter_col = outter_points()
    # 绘制五个截面
    sec1_paths = build_paths(base_dir, [
        '0+200/Z0+200.dat',
    ])
    sec1_pos, sec1_int, sec1_col = build_points(sec1_paths, 102, 'white')
    sec2_paths = build_paths(base_dir, [
        '0+275/Z0+275.dat',
    ])
    sec2_pos, sec2_int, sec2_col = build_points(sec2_paths, 108, 'white')
    sec3_paths = build_paths(base_dir, [
        '0+340.5/Z0+340.5.dat',
        '0+340.5/M_H_TY1.dat',
        '0+340.5/M_H_TY2.dat',
        '0+340.5/M_H_TY3.dat',
    ])
    sec3_pos, sec3_int, sec3_col = build_points(sec3_paths, 109, 'white')
    sec4_paths = build_paths(base_dir, [
        '0+450/Z0+450.dat',
    ])
    sec4_pos, sec4_int, sec4_col = build_points(sec4_paths, 110, 'white')
    sec5_paths = build_paths(base_dir, [
        '0+550/Z0+550.dat'
    ])
    sec5_pos, sec5_int, sec5_col = build_points(sec5_paths, 111, 'white')
    # 绘制 H 测点
    h_point_paths = build_paths(base_dir, [
        '0+200/M_H_1.dat',
        '0+200/M_H_5.dat',
        '0+275/M_H_2.dat',
        '0+275/M_H_6.dat',
        '0+275/M_H_9.dat',
        '0+275/M_H_12.dat',
        '0+275/M_H_14.dat',
        '0+340.5/M_H_3.dat',
        '0+340.5/M_H_7.dat',
        '0+340.5/M_H_10.dat',
        '0+340.5/M_H_13.dat',
        '0+340.5/M_H_15.dat',
        '0+340.5/M_H_LIN1.dat',
        '0+340.5/M_H_LIN2.dat',
        '0+340.5/M_H_LIN3.dat',
        '0+450/M_H_4.dat',
        '0+450/M_H_8.dat',
        '0+450/M_H_11.dat',
    ])
    h_point_pos, h_point_int, h_point_col = build_points(h_point_paths, 103, 'white')
    # 绘制 V 测点
    v_point_paths = build_paths(base_dir, [
        '0+200/M_V_DC1.dat',
        '0+200/M_V_DC2.dat',
        '0+200/M_V_XQ.dat',
        '0+275/M_V_XQ.dat',
        '0+340.5/M_V_DC3.dat',
        '0+340.5/M_V_DC5.dat',
        '0+340.5/M_V_XQ.dat',
        '0+450/M_V_XQ.dat',
        '0+550/M_V_XQ.dat'
    ])
    v_point_pos, v_point_int, v_point_col = build_points(v_point_paths, 104, 'white')
    # # 绘制 TY 
    # ty_point_paths = build_paths(base_dir, [
    #     '0+340.5/M_H_TY1.dat',
    #     '0+340.5/M_H_TY2.dat',
    #     '0+340.5/M_H_TY3.dat',
    # ])
    # ty_point_pos, ty_point_int, ty_point_col = build_points(ty_point_paths, 105, 'white')
    # 绘制 LIN
    lin_point_paths = build_paths(base_dir, [
        '0+340.5/M_H_LIN1.dat',
        '0+340.5/M_H_LIN2.dat',
        '0+340.5/M_H_LIN3.dat',
    ])
    lin_point_pos, lin_point_int, lin_point_col = build_points(lin_point_paths, 106, 'white')

    other_than_all_pos = np.concatenate((
        outter_pos,
        sec1_pos,
        sec2_pos,
        sec3_pos,
        sec4_pos,
        sec5_pos,
        h_point_pos,
        v_point_pos,
        lin_point_pos
    ))
    other_pos, other_int, other_col = other_points(other_than_all_pos)

    position = np.concatenate((
        outter_pos,
        sec1_pos,
        sec2_pos,
        sec3_pos,
        sec4_pos,
        sec5_pos,
        h_point_pos,
        v_point_pos,
        lin_point_pos,
        other_pos
    ))
    intensity = np.concatenate((
        outter_int,
        sec1_int,
        sec2_int,
        sec3_int,
        sec4_int,
        sec5_int,
        h_point_int,
        v_point_int,
        lin_point_int,
        other_int
    ))
    rgb = np.concatenate((
        outter_col,
        sec1_col,
        sec2_col,
        sec3_col,
        sec4_col,
        sec5_col,
        h_point_col,
        v_point_col,
        lin_point_col,
        other_col
    ))
    write_las(las_path, position, intensity, rgb)

if __name__ == '__main__':
    base_dir = './data/5截面和测点'
    las_path = './out/5断面和测点-v2.las'
    main()
