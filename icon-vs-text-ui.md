# Icon hay chữ cho nút hành động/điều hướng

Nguồn: `notes` (ghi lúc 2026-08-14, sau khi đổi nút "về hôm nay" ở Calendar
từ chữ sang icon `CalendarDays`). Ghi lại quy tắc để project mobile-first
khác áp dụng luôn, đỡ phải quyết định lại từ đầu mỗi lần thêm nút mới.

## Quy tắc

**Ưu tiên icon hơn chữ** cho nút hành động/điều hướng trên app mobile-first
(bàn phím/màn hình nhỏ, ít chỗ). Icon nhận diện nhanh hơn chữ, không tốn
chiều ngang, không cần dịch i18n.

**Chỉ giữ chữ khi:**

- Icon một mình gây mơ hồ, không có convention phổ biến để đoán nghĩa
  (vd nút "Lưu"/"Huỷ" — không có icon chuẩn nào ai cũng hiểu ngay).
- Tab bar chính (bottom nav) — dùng cả icon + label, vì đây là nơi user cần
  chắc chắn 100% không bấm nhầm mục, và có đủ chỗ hiển thị cả hai.
- Nút hiếm khi bấm nhưng hậu quả lớn (xoá tài khoản, xuất dữ liệu) — chữ rõ
  ràng hơn để tránh bấm nhầm.

**Khi dùng icon-only:** luôn kèm `aria-label` mô tả hành động (screen
reader + tooltip fallback), không được để icon mồ côi không có label nào.

## Ví dụ (từ `notes`)

```tsx
// Trước: chữ trong nút text, chiếm chỗ, phải i18n cả 2 ngôn ngữ
<button onClick={goToday}>
  {monthLabel}
  <span className="text-primary">{t.calendar_go_today}</span>
</button>

// Sau: icon riêng, chỉ hiện khi cần (đang xem tháng khác), có aria-label
<button onClick={goToday} aria-label={t.calendar_go_today}>
  <CalendarDays size={16} />
</button>
```

Xem thêm [icon-libs.md](icon-libs.md) cho lib icon dùng (lucide-react).
