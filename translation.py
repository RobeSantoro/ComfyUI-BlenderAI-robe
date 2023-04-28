"""
translations_tuple = (
    (
        ("*", ""),  # (msgctxt, msgid)
        ((), ()),   # (sources, gen_comments)
        ("fr_FR", "Project-Id-Version: ", (False, ("D.", "D.", "D.", "D."))),  # (lang, translation, (is_fuzzy, comments))
    ),
    (
        ("Operator", "Render: Copy Settings"),
        (("bpy.types.SCENE_OT_render_copy_settings",), ()),
        ("fr_FR", "Rendu : copier réglages", (False, ())),
    ),
    (
        ("*", "Copy render settings from current scene to others"),
        (("bpy.types.SCENE_OT_render_copy_settings",), ()),
        ("fr_FR", "Some translation text", (False, ())),
    ),
)

translations_dict = {}
for msg in translations_tuple:
    key = msg[0]  # (msgctxt, msgid)
    for lang, trans, (is_fuzzy, comments) in msg[2:]:  # (lang, translation, (is_fuzzy, comments))
        if trans and not is_fuzzy:
            translations_dict.setdefault(lang, {})[key] = trans
td = {'fr_FR': {
    ('*', ''): 'Project-Id-Version: ',
    ('Operator', 'Render: Copy Settings'): 'Rendu : copier réglages',
    ('*', 'Copy render settings from current scene to others'): 'Some translation text'
}
}
"""

ctxt = "SDN"

other = {
    # SDNode/manager.py
    "Kill Last ComfyUI Process": "关闭上次打开的ComfyUI",
    "ComfyUI Path Not Found": "ComfyUI路径不存在",
    "Server Launching": "服务启动中...",
    "python interpreter not found": "未找到 python解释器",
    "Ensure that the python_embeded located in the same level as ComfyUI dir": "请确保python_embeded文件夹存放于ComfyUI路径同级目录",
    "Model Path": "当前ComfyUI路径",
    "Error: Out of VRam, try restart blender": "错误:显存不足, 请重启blender",
    "Server Launched": "服务启动成功!",
    "Add Task": "添加任务",
    "Server Not Launched, Add Task Failed": "服务未启动, 任务添加失败",
    "Please Check ComfyUI Directory": "请检查ComfyUI路径",
    "Server Not Launched": "服务未启动",
    "Add Result": "获取结果",
    "Submit Task": "提交任务",
    "Invalid Node Connection":"无效节点连接",
    "Node Connection Error": "节点连接错误",
    "Input Image Error":"输入图像错误",
    "Params Not Changed":"参数未变更",
    "Node Tree Not Executed, May Caused by:": "节点树未被执行, 可能原因:",
    "Proc Resutl":"处理结果",
    "Ran Node": "运行节点",
    # SDNode/nodes.py
    "icon path load error": "预览图配置解析失败",
    "|IGNORED|": "|已忽略|",
    "Not Found Item": "未找到项",
    "Load": "载入",
    "Params not matching with current node": "参数与当前节点不匹配",
    "Params Loading Error": "参数载入错误",
    "Remove Link": "移除连接",
    "Parsing Node Start": "解析节点中...",
    "Server Launch Failed": "服务启动失败, 使用缓存节点信息数据",
    "None Input":"节点输入",
    "Parsing Node Finished!": "解析节点完成!",
    "Render": "渲染",
    "Post Function": "后处理函数",
    "Load Preview Image": "加载预览图",
    "  Select mask Objects": "  选中mask物体(可多选)",
    "  Select mask Collections": "  选中mask集合(可多选)",
    "Set Image Path of Render Result(.png)": "设置摄像机渲染图像的保存位置及文件名(.png)，如已设置请忽略",
    # __init__.py
    "Image not found or format error(png only)": "魔法图鉴不存在或格式不正确(仅png)",
    "Execute Node Tree": "运行节点树",
    "Node Tree": "节点树",
    "Save": "保存",
    "Delete": "删除",
    "Replace Node Tree": "替换节点树",
    "Node Group": "节点",
    "Append Node Group": "追加节点",
    "Pending / Running": "排队 / 运行",
    "Adjust node tree and try again": "请调整后重新执行节点树",
    "Load from Image": "加载魔法图鉴",
    "Preset": "法典",
    "exists, Click Ok to Overwrite!": "已存在, 确认将覆盖!",
    "Click Outside to Cancel!": "单击空白处取消!",
    "will be removed?": "即将消亡?",
    "Click Folder Icon to Select Image:": "点击文件夹图标选择魔法图鉴:",
    "Preset Not Selected!": "没有选择法典!",
    "Invalid Preset Name!":"无效的法典名!",
    "Removed": "移除成功",
    "Presets": "预设",
    "Open NodeGroup Presets Folder": "打开节点预设文件夹",
    "Open NodeTree Presets Folder": "打开节点树预设文件夹",
    "Groups Directory": "节点文件夹",
    "Presets Directory": "预设文件夹",
    "Open Addon Preference": "打开插件设置",
    "Restart ComfyUI": "重启ComfyUI",
    "Launch ComfyUI": "打开ComfyUI",
    "Random All": "随机所有"
}

other_cn_en = {
    
}
lang_text = {
    "zh_CN": {
        **other,
        # 分类
        "latent": "潜空间",
        "advanced": "高级",
        "_for_testing": "测试",
        "upscaling": "缩放",
        "postprocessing": "后处理",
        # 其他
        "text": "文本",
        "filename_prefix": "前缀",
        "output_dir": "输出路径",
        "exe_rand": "每次运行节点随机",
        "enable": "开",
        "disable": "关",
        "samples": "采样",
        "sdn_width": "宽",
        "sdn_height": "高",
        "batch_size": "队列大小",
        "images": "图像",
        "IMAGE": "图像",
        # "vae": "变分数据",
        # "VAE": "变分模型",
        # "nt": "浅空间数据模型",
        # "LATENT": "浅空间数据模型",
        "pixels": "像素",
        # "MASK": "遮罩",
        # Node name
        "KSampler": "K采样器",
        "CheckpointLoader": "Checkpoint加载器",
        "CheckpointLoaderSimple": "Checkpoint简易加载器",
        "CLIPTextEncode": "CLIP文本编码",
        "CLIPSetLastLayer": "CLIP设置最后一层",
        "VAEDecode": "VAE解码",
        "VAEEncode": "VAE编码",
        "VAEEncodeForInpaint": "VAE内补编码器",
        "VAELoader": "VAE加载器",
        "EmptyLatentImage": "空Latent图像",
        "LatentUpscale": "Latent放大",
        "SaveImage": "保存图像",
        "PreviewImage": "预览图像",
        "LoadImage": "加载图像",
        "LoadImageMask": "加载图像遮罩",
        "ImageScale": "图像缩放",
        "ImageInvert": "图像反转",
        # ？
        "ConditioningCombine": "条件合并",
        "ConditioningSetArea": "条件区域",
        "KSamplerAdvanced": "高级K采样器",
        "SetLatentNoiseMask": "设置Latent噪波遮罩",
        "LatentComposite": "Latent复合",
        "LatentRotate": "Latent旋转",
        "LatentFlip": "Latent翻转",
        "LatentCrop": "Latent修剪",
        "LoraLoader": "Lora加载器",
        "CLIPLoader": "CLIP加载器",
        "CLIPVisionEncode": "CLIP视觉编码",
        "StyleModelApply": "风格模型应用",
        "ControlNetApply": "ControlNet应用",
        "ControlNetLoader": "ControlNet加载器",
        "DiffControlNetLoader": "另一种ControlNet加载器",
        "T2IAdapterLoader": "文生图适配加载器",
        "StyleModelLoader": "风格模型加载器",
        "CLIPVisionLoader": "CLIP视觉加载器",
        "VAEDecodeTiled": "VAE平铺化解码",
        "VAEEncodeTiled": "VAE平铺化编码",
        # Other
        "Add Node": "添加节点",
        "Add Group": "添加组",
        "Add Node": "添加节点",
        "sampling": "采样",
        "loaders": "加载器",
        "latnet": "latnet",
        "conditioning": "条件",
        "image": "图像",
        "utils": "实用工具",
        "Reroute": "连线改道",
        "utils": "实用工具",
        # node in
        "model": "模型",
        "positive": "正向",
        "negative": "反向",
        "latent_image": "latent图像",
        "seed": "随机种",
        "cfg": "cfg",
        "sampler_name": "采样器",
        "scheduler": "调度器",
        "denoise": "降噪",
        "LTAENT": "LTAENT",
        "Value": "值",
        "OK": "确认",
        "add_noise": "添加噪波",
        #？
        "noise_seed": "噪波随机种",
        "Random seed after every gen": "每次生成后随机化随机种",
        "steps": "步数",
        "start_at_step": "开始步数",
        "end_at_step": "结束步数",
        # ？
        "return_with_leftover_noise": "返回残余噪波",
        "config_name": "配置名称",
        "ckpt_name": "ckpt名称",
        "MODEL": "模型",
        # ？
        "CLIP": "CLIP(语言-图像对比预训练)",
        "VAE": "VAE",
        "vae_name": "vae名称",
        "clip": "CLIP(语言-图像对比预训练)",
        "strength_model": "模型强度",
        "strength_clip": "CLIP强度",
        "undefined": "未定义",
        "control_net_name": "controlnet名称",
        "CONTROL_NET": "CONTROLNET",
        "t2i_adapter_name": "文生图适配器名称",
        "style_model_name": "风格模型名称",
        "STYLE_MODEL": "风格模型",
        "clip_name": "CLIP名称",
        "CLIP_VISION": "视觉CLIP",
        "model_name": "模型名称",
        "UPSCALE_MODEL": "放大模型",
        "style_model": "风格模型",
        "CLIPTextEncode": "CLIP文本编码器",
        # ?
        "CLIPSetLastLayer": "CLIP设置最后一层",
        "clip_vision": "视觉CLIP",
        "CLIP_VISION_OUTPUT": "视觉CLIP输出",
        "clip_vision_output": "视觉CLIP输出",
        "conditioning": "条件",
        "stop_at_clip_layer": "停止在clip层",
        "conditioning_1": "条件1",
        "conditioning_2": "条件2",
        "witch": "宽",
        "height": "高",
        "strength": "强度",
        "control_net": "controlnet",
        "inpaint": "内补绘制",
        "transform": "变换",
        "CONDITIONING": "条件",
        "unCLIPCheckpointLoader": "逆CLIPCheckpoint加载器",
        "UpscaleModelLoader": "放大模型加载器",
        "unCLIPConditioning": "逆CLIP条件",
        "noise_augmentation": "噪波增强",
        "90 degrees": "90度",
        "180 degrees": "180度",
        "270 degrees": "270度",
        "flip_method": "翻转方法",
        "x-axis: vertically": "X轴:垂直",
        "y-axis: horizontally": "Y轴:水平",
        "crop": "裁剪",
        "nearest-exact": "邻近-精确",
        "bilinear": "双线性",
        # ？
        "feather": "羽化",
        "samples_to": "采样到",
        "samples_from": "采样自",
        "ImageUpscaleWithModel": "图像通过模型放大",
        "upscale_model": "放大模型",
        "ImageBlend": "图像混合",
        "blend_factor": "混合系数",
        "blend_mode": "混合模式",
        "image1": "图像1",
        "image2": "图像2",
        "overlay": "叠加",
        "soft_light": "柔光",
        "ImageBlur": "图像模糊",
        "blur_radius": "模糊半径",
        "ImageQuantize": "图像量化",
        "colors": "颜色数",
        "dither": "抖动",
        "floyd-steinberg": "弗洛伊德-斯坦伯格抖动算法",
        "ImageSharpen": "图像锐化",
        "sharpen_radius": "锐化半径",
        "ImagePadForOutpaint": "外补绘画填充画板",
        "feathering": "羽化",
        # ？token merging
        "TomePatchModel": "Token合并修补模型",
        "preprocessors": "预处理器",
        "edge_line": "边缘线",
        "pose": "姿态",
        "normal_depth_map": "法向深度映射",
        "semseg": "语义分割",
        "face_mesh": "面部网格",
        "color_style": "颜色风格",
        "CannyEdgePreprocessor": "Canny(细致线)预处理器",
        "low_threshold": "低阈值",
        "high_threshold": "高阈值",
        "l2gradient": "L2范数",
        "M-LSDPreprocessor": "M-LSD(线段)预处理器",
        # ？
        "score_threshold": "刻痕阈值",
        "dist_threshold": "距离阈值",
        # Holistically-Nested Edge Detection
        "HEDPreprocessor": "HED(模糊线)预处理器",
        "ScribblePreprocessor": "Scribble(涂鸦线)预处理器",
        "FakeScribblePreprocessor": "FakeScribble(伪涂鸦)预处理器",
        "BinaryPreprocessor": "Binary二值化预处理器",
        # Pixel Difference Networks for Efficient Edge Detection
        "PiDiNetPreprocessor": "PidiNet(模糊线)预处理器",
        "OpenposePreprocessor": "Openpose(姿态)预处理器",
        "MediaPipe-HandPosePreprocessor": "MediaPipe-HandPose(手部姿态)预处理器",
        "detect_pose": "检测姿态",
        "detect_hand": "检测手部",
        "detect_hands": "检测手部",
        "MiDaS-DepthMapPreprocessor": "MiDaS-DepthMap(深度映射)预处理器",
        "MiDaS-NormalMapPreprocessor": "MiDaS-NormalMap(法向映射)预处理器",
        "bg_threshold": "背景阈值",
        "LeReS-DepthMapPreprocessor": "LeReS-DepthMap(深度映射)预处理器",
        "rm_nearest": "前景移除",
        "rm_background": "背景移除",
        "SemSegPreprocessor": "SemSeg(语义分割)预处理器",
        "MediaPipe-FaceMeshPreprocessor": "MediaPipe-FaceMesh(面部网格)预处理器",
        "max_faces": "最大面数",
        "min_confidence": "最小置信度",
        "ColorPreprocessor": "Color颜色预处理",
        "lora_name": "lora名称",
        "LatentCompositeMasked": "Latent遮罩复合",
        "MaskToImage": "遮罩转图像",
        "ImageToMask": "图像转遮罩",
        "SolidMask": "纯块遮罩",
        "InvertMask": "反转遮罩",
        "CropMask": "遮罩裁剪",
        "MaskComposite": "遮罩混合",
        "FeatherMask": "羽化遮罩",
        "DiffusersLoader": "Diffusers(扩散)载入器",
        "model_path": "模型路径",
        "GLIGENLoader": "GLIGEN加载器",
        "gligen_name": "GLIGEN名称",
        "gligen": "GLIGEN基于语言的图像生成",
        "safe": "增稳",
        "LatentFromBatch": "从队列获取Latent",
        "GLIGENTextBoxApply": "GLIGEN文本框应用",
        "conditioning_to": "条件到",
        "gligen_textbox_model": "GLIGEN文本框模型",
        "HED-v11-Preprocessor": "HED(模糊线)-v11-预处理器",
        "PiDiNet-v11-Preprocessor": "PidiNet(模糊线)-v11-预处理器",
        "BAE-NormalMapPreprocessor": "BAE-NormalMap(法向映射)预处理器",
        "Zoe-DepthMapPreprocessor": "Zoe-DepthMap(深度映射)预处理器",
        "left": "左",
        "top": "上",
        "right": "右",
        "bottom": "下",
        "batch_index": "队列索引",
        "normal": "通用",
        "ratio": "比率",
        "rotation": "旋转",
        "destination": "目标",
        "source": "源",
        "upscale_method": "放大方法",
        "sigma": "sigma西格玛系数",
        "channel": "通道",
        "value": "明度",
        "version": "版本",
        "threshold": "临界值(0-255)",
        "detect_body": "检测身体",
        "detect_face": "检测面部",
        "HypernetworkLoader": "Hypernetwork超网络加载器",
        "hypernetwork_name": "hypernetwork超网络名称",
    }
}
cat = {'default_real': None,
       'default': '*',
       'operator_default': 'Operator',
       'ui_events_keymaps': 'UI_Events_KeyMaps',
       'plural': 'Plural',
       'id_action': 'Action',
       'id_armature': 'Armature',
       'id_brush': 'Brush',
       'id_camera': 'Camera',
       'id_cachefile': 'CacheFile',
       'id_collection': 'Collection',
       'id_curve': 'Curve',
       'id_fs_linestyle': 'FreestyleLineStyle',
       'id_gpencil': 'GPencil',
       'id_curves': 'Curves',
       'id_id': 'ID',
       'id_image': 'Image',
       'id_shapekey': 'Key',
       'id_light': 'Light',
       'id_library': 'Library',
       'id_lattice': 'Lattice',
       'id_mask': 'Mask',
       'id_material': 'Material',
       'id_metaball': 'Metaball',
       'id_mesh': 'Mesh',
       'id_movieclip': 'MovieClip',
       'id_nodetree': 'NodeTree',
       'id_object': 'Object',
       'id_paintcurve': 'PaintCurve',
       'id_palette': 'Palette',
       'id_particlesettings': 'ParticleSettings',
       'id_pointcloud': 'PointCloud',
       'id_lightprobe': 'LightProbe',
       'id_scene': 'Scene',
       'id_screen': 'Screen',
       'id_sequence': 'Sequence',
       'id_simulation': 'Simulation',
       'id_speaker': 'Speaker',
       'id_sound': 'Sound',
       'id_texture': 'Texture',
       'id_text': 'Text',
       'id_vfont': 'VFont',
       'id_volume': 'Volume',
       'id_world': 'World',
       'id_workspace': 'WorkSpace',
       'id_windowmanager': 'WindowManager',
       'editor_view3d': 'View3D'
       }

translations_dict = {}
for cultral, translations in lang_text.items():
    translations_dict[cultral] = {}
    for word, translation in translations.items():
        translations_dict[cultral][(ctxt, word)] = translation
        translations_dict[cultral][(None, word)] = translation
