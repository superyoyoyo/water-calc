import streamlit as st

# 設定網頁標題和圖示
st.set_page_config(page_title="軟水計算機", page_icon="💧")

st.title("💧 軟化樹脂造水量計算")
st.write("輸入數據，自動計算安全採水量")

# --- 輸入區 ---
with st.container():
    col1, col2 = st.columns(2)
    # X: 交換容量
    with col1:
        capacity_per_liter = st.number_input("每公升樹脂交換量 (X)", value=40.0, step=1.0)
    # Y: 樹脂量
    with col2:
        resin_volume = st.number_input("樹脂總量 (Y) 公升", value=150.0, step=10.0)
    
    # Z: 硬度
    hardness = st.number_input("自來水硬度 (Z) ppm", value=100.0, step=10.0)

# --- 計算按鈕與邏輯 ---
if st.button("開始計算", type="primary", use_container_width=True):
    if hardness <= 0:
        st.error("❌ 硬度必須大於 0")
    else:
        # 計算邏輯 (與您原本的相同)
        theoretical_tons = (capacity_per_liter * resin_volume) / hardness
        safe_tons = theoretical_tons * 0.7
        
        # --- 顯示結果 ---
        st.markdown("---")
        st.subheader("📊 計算結果")
        
        # 使用 Metric 元件顯示比較漂亮的大數字
        c1, c2 = st.columns(2)
        c1.metric("理論極限造水", f"{theoretical_tons:.2f} 噸")
        c2.metric("建議設定 (70%)", f"{safe_tons:.2f} 噸", delta="安全設定")
        
        st.success(f"✅ 建議您將流量計設定在 **{safe_tons:.2f} 噸** 進行再生。")