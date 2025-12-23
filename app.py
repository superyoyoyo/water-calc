import streamlit as st

# 1. 頁面基本設定
st.set_page_config(page_title="水處理計算機", page_icon="💧")
st.title("💧水處理工程計算")

# 2. 建立側邊欄或主畫面的選單
# 這裡我們做一個下拉選單，讓使用者選擇要算什麼
calculation_type = st.selectbox(
    "請選擇計算項目：",
    ["軟化系統 (Softener)", "滿床系統 (2BT)", "混床系統 (MB)" ,"FRP桶濾材計算"]
)

st.markdown("---") # 畫一條分隔線

# ==========================================
# 模式 A: 軟化系統 (這是原本的功能)
# ==========================================
if calculation_type == "軟化系統 (Softener)":
    st.header("🧂 軟化系統計算")
    
    # [輸入區]
    col1, col2 = st.columns(2)
    with col1:
        x = st.number_input("樹脂交換容量 (g/L)", value=40.0)
    with col2:
        y = st.number_input("樹脂總量 (L)", value=150.0)
    z = st.number_input("原水總硬度 (ppm CaCO3)", value=100.0)

    # [計算與結果]
    if st.button("計算軟化產能"):
        if z <= 0:
            st.error("硬度必須大於 0")
        else:
            ans = (x * y) / z
            safe_ans = ans * 0.7
            st.success(f"建議採水量：**{safe_ans:.2f}** 噸")

# ==========================================
# 模式 B: 滿床系統 (這是新增的示範)
# ==========================================
elif calculation_type == "滿床系統 (2BT)":
    st.header("📦 滿床系統計算")
    
    # 1. 設定輸入框 (Input)
        col1, col2 = st.columns(2)
    with col1:
        x = st.number_input("樹脂交換容量 (g/L)", value=40.0)
    with col2:
        y = st.number_input("樹脂總量 (L)", value=150.0)
    z = st.number_input("原水總硬度 (ppm CaCO3)", value=100.0)

    # [計算與結果]
    if st.button("計算軟化產能"):
        if z <= 0:
            st.error("硬度必須大於 0")
        else:
            ans = (x * y) / z
            safe_ans = ans * 0.7
            st.success(f"建議採水量：**{safe_ans:.2f}** 噸")
# ==========================================
    # 2. 設定按鈕與公式 (Logic)
    if st.button("計算滿床產能"):
        # 圓柱體積公式 V = π * r² * h
        import math
        volume_cm3 = math.pi * (radius ** 2) * height
        volume_liter = volume_cm3 / 1000  # 換算成公升
        
        # 3. 顯示結果 (Output)
        st.write(f"桶槽截面積：{math.pi * (radius**2):.2f} cm²")
        st.success(f"所需樹脂量：**{volume_liter:.2f}** 公升")
        col1, col2 = st.columns(2)
    
# 模式 C: 陰離子系統 (預留給您填寫)
# ==========================================
elif calculation_type == "陰離子系統 (Anion)":
    st.header("🧪 陰離子交換計算")
    st.write("🚧 功能開發中，請依照上方格式自行複製修改程式碼...")

# ==========================================
# 模式 D: 混床 (預留給您填寫)
# ==========================================
elif calculation_type == "混床系統 (MB)":
    st.header("🔄 混床系統計算")
    st.write("🚧 功能開發中...")
# ==========================================
# 模式 E: FRP 桶型號計算 (新增功能)
# ==========================================
elif calculation_type == "FRP桶濾材計算":
    st.header("🛢️ FRP 桶濾材量計算")
    st.info("輸入型號 (如 1054)，自動估算濾材公升數")

    # [輸入區]
    col1, col2 = st.columns([2, 1])
    with col1:
        model_code = st.text_input("請輸入 FRP 桶型號", value="1054", placeholder="例如：1054, 1354")
    with col2:
        # 讓您可以微調填充率 (預設 70%)
        fill_percent = st.number_input("填充比例 (%)", value=70, step=5)

    # [計算邏輯]
    if st.button("計算填充量"):
        # 1. 檢查輸入格式是否為數字
        if not model_code.isdigit() or len(model_code) < 3:
            st.error("❌ 格式錯誤！請輸入至少 3 碼數字 (例如 844 或 1054)")
        else:
            try:
                # 2. 拆解型號 (最後兩碼是高度，前面是直徑)
                h_inch = int(model_code[-2:])   # 取最後兩個字
                d_inch = int(model_code[:-2])   # 取前面剩下的字
                
                # 3. 計算體積 (圓柱公式)
                import math
                radius_inch = d_inch / 2
                area_sq_inch = math.pi * (radius_inch ** 2)
                volume_cu_inch = area_sq_inch * h_inch
                
                # 4. 單位換算 (1 立方英吋 = 0.016387 公升)
                total_liters = volume_cu_inch * 0.016387
                
                # 5. 計算建議填充量
                fill_liters = total_liters * (fill_percent / 100)
                
                # 6. 計算包數 (假設一包 25L)
                bags = fill_liters / 25
                
                # [顯示結果]
                st.markdown("---")
                st.subheader(f"📊 型號 {model_code} 計算結果")
                
                c1, c2, c3 = st.columns(3)
                c1.metric("直徑 x 高度", f"{d_inch}\" x {h_inch}\"")
                c2.metric("全桶總容積", f"{total_liters:.1f} L")
                c3.metric(f"建議填充量 ({fill_percent}%)", f"{fill_liters:.1f} L", delta=f"約 {bags:.1f} 包")
                
                # 額外資訊：顯示常用的 65%~75% 範圍
                st.caption(f"💡 參考：{total_liters*0.65:.1f}L (65%) ~ {total_liters*0.75:.1f}L (75%)")

            except Exception as e:
                st.error(f"計算發生錯誤：{e}")











