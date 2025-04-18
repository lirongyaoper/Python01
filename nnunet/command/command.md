# 1. 预训练
nnUNetv2_plan_and_preprocess -d DATASET -pl nnUNetPlannerResEncXL
```bash
nnUNetv2_plan_and_preprocess -d 001 \
  -pl nnUNetPlannerResEncXL \
  --verify_dataset_integrity
```


# 2.训练
## 第一阶段训练（2D U-Net）

```bash
nnUNetv2_train 001 2d 0 -p nnUNetResEncUNetLPlans &&
nnUNetv2_train 001 2d 1 -p nnUNetResEncUNetLPlans &&
nnUNetv2_train 001 2d 2 -p nnUNetResEncUNetLPlans &&
nnUNetv2_train 001 2d 3 -p nnUNetResEncUNetLPlans &&
nnUNetv2_train 001 2d 4 -p nnUNetResEncUNetLPlans

```


## 阶段2：训练低分辨率模型（3d_lowres）
nnUNetv2_train DATASET_ID 3d_lowres 0 -tr nnUNetTrainerResEncXL -p nnUNetResEncUNetXLPlans --npz
```bash
nnUNetv2_train 001 3d_lowres 0 -p nnUNetResEncUNetLPlans &&
nnUNetv2_train 001 3d_lowres 1 -p nnUNetResEncUNetLPlans &&
nnUNetv2_train 001 3d_lowres 2 -p nnUNetResEncUNetLPlans &&
nnUNetv2_train 001 3d_lowres 3 -p nnUNetResEncUNetLPlans &&
nnUNetv2_train 001 3d_lowres 4 -p nnUNetResEncUNetLPlans
```
## 阶段3：级联全分辨率训练（需完成所有5折）
```bash
nnUNetv2_train 001 3d_fullres 0 -p nnUNetResEncUNetXLPlans &&
nnUNetv2_train 001 3d_fullres 1 -p nnUNetResEncUNetXLPlans &&
nnUNetv2_train 001 3d_fullres 2 -p nnUNetResEncUNetXLPlans &&
nnUNetv2_train 001 3d_fullres 3 -p nnUNetResEncUNetXLPlans &&
nnUNetv2_train 001 3d_fullres 4 -p nnUNetResEncUNetXLPlans
```
## 阶段4：级联全分辨率训练（需完成所有5折）
```bash
nnUNetv2_train 001 3d_cascade_fullres 0 -p nnUNetResEncUNetXLPlans &&
nnUNetv2_train 001 3d_cascade_fullres 1 -p nnUNetResEncUNetXLPlans &&
nnUNetv2_train 001 3d_cascade_fullres 2 -p nnUNetResEncUNetXLPlans &&
nnUNetv2_train 001 3d_cascade_fullres 3 -p nnUNetResEncUNetXLPlans &&
nnUNetv2_train 001 3d_cascade_fullres 4 -p nnUNetResEncUNetXLPlans
```
# 3.选择最好模型




# 其他训练
```bash
 nnUNetv2_predict -i /home/lirongyaoper/Documents/train_self/ -o /home/lirongyaoper/Documents/label_self/ -d 1 -c 3d_fullres --save_probabilities
```