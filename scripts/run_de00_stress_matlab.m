% Run CIEDE2000 (DE00) STRESS on dataset_comprehensive.mat in MATLAB using
% Merlin's reference implementation: data_XYZ2CDE.m (PostDoc_Handover).
% Also optionally compares against Python export results/de00_python.csv.
%
% Usage (MATLAB):
%   run('/Users/merlin/WorkSpace/Python/Meta-Color/scripts/run_de00_stress_matlab.m');

clear; clc;

% Absolute paths (edit if your checkout differs).
repo_root = "/Users/merlin/WorkSpace/Python/Meta-Color";
matlab_ref_root = "/Users/merlin/WorkSpace/Matlab/testing/PostDoc_Handover";

if exist(matlab_ref_root, "dir") ~= 7
    error("Missing MATLAB reference folder: %s", matlab_ref_root);
end
addpath(genpath(matlab_ref_root));

fprintf("================================================================================\n");
fprintf("MATLAB DE00 STRESS on dataset_comprehensive.mat\n");
fprintf("================================================================================\n");

data_path = fullfile(repo_root, "dataset_comprehensive.mat");
if exist(data_path, "file") ~= 2
    error("Missing dataset file: %s", data_path);
end

data = load(data_path);
dc = data.dataset_comprehensive;

% dataset_comprehensive is a cell array (rows: datasets, row 1 is header).
for r = 2:size(dc, 1)
    dataset_id = string(dc{r, 2});
    xyz_data = dc{r, 3}; % Nx10: [XYZw XYZ1 XYZ2 dV]

    dV = xyz_data(:, 10);

    % data_XYZ2CDE expects Nx10: [XYZw, XYZc, XYZs, DV]
    La_Yb_surround = {20, 20, 'avg'};
    DEDLDCDH = data_XYZ2CDE(xyz_data, 'de00', La_Yb_surround);
    dE00 = DEDLDCDH(:, 1);
    stress = STRESS_closed_form(dE00, dV);

    fprintf("%18s | n=%5d | STRESS=%7.3f\n", dataset_id, size(xyz_data, 1), stress);
end

% Try an optional comparison if the Python export exists.
py_csv = fullfile(repo_root, "results", "de00_python.csv");
if exist(py_csv, "file") == 2
    fprintf("--------------------------------------------------------------------------------\n");
    fprintf("Comparing to Python export: %s\n", py_csv);
    T = readtable(py_csv);

    XYZw = [T.xyzw_X, T.xyzw_Y, T.xyzw_Z];
    XYZ1 = [T.xyz1_X, T.xyz1_Y, T.xyz1_Z];
    XYZ2 = [T.xyz2_X, T.xyz2_Y, T.xyz2_Z];
    dV = T.dV;

    data10 = [XYZw, XYZ1, XYZ2, dV];
    La_Yb_surround = {20, 20, 'avg'};
    DEDLDCDH = data_XYZ2CDE(data10, 'de00', La_Yb_surround);
    dE00_m = DEDLDCDH(:, 1);

    diff_current = dE00_m - T.de00_py_current;
    diff_wp = dE00_m - T.de00_py_wp;

    fprintf("Max |MATLAB - Python(current)|: %.6g\n", max(abs(diff_current)));
    fprintf("Mean|MATLAB - Python(current)|: %.6g\n", mean(abs(diff_current)));
    fprintf("RMS |MATLAB - Python(current)|: %.6g\n", sqrt(mean(diff_current.^2)));

    fprintf("Max |MATLAB - Python(wp)|: %.6g\n", max(abs(diff_wp)));
    fprintf("Mean|MATLAB - Python(wp)|: %.6g\n", mean(abs(diff_wp)));
    fprintf("RMS |MATLAB - Python(wp)|: %.6g\n", sqrt(mean(diff_wp.^2)));

    fprintf("STRESS MATLAB:        %.6g\n", STRESS_closed_form(dE00_m, dV));
    fprintf("STRESS Python current %.6g\n", STRESS_closed_form(T.de00_py_current, dV));
    fprintf("STRESS Python wp      %.6g\n", STRESS_closed_form(T.de00_py_wp, dV));
end

fprintf("================================================================================\n");

% ------------------------------------------------------------------------------
% Local functions (keep this file self-contained)
% ------------------------------------------------------------------------------

function stress = STRESS_closed_form(dE, dV)
    dE = dE(:);
    dV = dV(:);
    stress = 100 * sqrt(max(0, 1 - (sum(dE .* dV)^2) / (sum(dE.^2) * sum(dV.^2))));
end
