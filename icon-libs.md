# Thư viện icon nhẹ, đẹp, tree-shake tốt

Nguồn: `notes` (ghi lúc 2026-08-14). Đã chọn **lucide-react**, dùng trong
`src/App.tsx` và các screen. Trước đó `notes` tự vẽ SVG trong `src/icons.tsx`
để né dependency — đổi sang lucide khi số icon cần dùng tăng lên, tự vẽ tiếp
không còn đáng công. File này ghi lại các lựa chọn khác để project sau tham
khảo, đỡ tra cứu lại từ đầu.

Cả 4 đều export mỗi icon là 1 component riêng nên **tree-shake tự nhiên**
(bundler chỉ đóng gói icon thật sự import), không cần cấu hình gì thêm.

## 1. lucide-react — đang dùng (notes)

```
pnpm add lucide-react
```

```tsx
import { Calendar, Settings, Trash2 } from "lucide-react";

<Calendar size={20} />;
```

- ~1500+ icon, style outline nhất quán (stroke 2px), nét bo tròn nhẹ — hợp
  giao diện mobile-first, bo góc của `ui-kit`.
- Mỗi icon component nhận thẳng `size`, `color`, `strokeWidth` — không cần
  wrapper.
- Phổ biến nhất hiện tại (fork của feather-icons, cập nhật đều), dễ tra cứu
  tên icon trên lucide.dev.
- ISC license.

## 2. @tabler/icons-react — nhiều icon nhất, không dùng

```
pnpm add @tabler/icons-react
```

Style outline tương tự lucide, nhưng ~5900 icon (gấp gần 4 lần). Đáng cân
nhắc nếu lucide thiếu icon cần (domain đặc thù: kế toán, y tế, bản đồ...).
Nặng hơn lucide một chút do tên export dài + số lượng file nhiều, nhưng vẫn
tree-shake tốt nên không ảnh hưởng bundle thật sự dùng. MIT.

## 3. @heroicons/react — khớp Tailwind nhất, không dùng

```
pnpm add @heroicons/react
```

Của chính Tailwind Labs, 2 style (`/24/outline`, `/24/solid`) + bản `/20/solid`
cho icon nhỏ. Ít icon hơn hẳn (~300) nhưng vẽ tay kỹ, khớp gu Tailwind. Import
theo path riêng từng style:

```tsx
import { TrashIcon } from "@heroicons/react/24/outline";
```

Đáng chọn nếu app đã 100% Tailwind-native và không cần nhiều icon lạ. Không
chọn cho `notes` vì thư viện quá ít icon (thiếu icon ghi âm/máy ảnh phù hợp).

## 4. phosphor-react — nhiều weight, không dùng

```
pnpm add phosphor-react
```

Mỗi icon có 6 weight (`thin/light/regular/bold/fill/duotone`), style bo tròn
mềm mại hơn lucide/tabler — hợp app cá nhân/nhật ký muốn giao diện dễ thương
hơn là app công việc nghiêm túc. Đổi weight qua prop `weight`, không cần đổi
import. Đáng cân nhắc lại nếu sau này muốn đổi hướng thẩm mỹ của `notes` sang
mềm mại hơn thay vì outline chuẩn.

## Cách đổi lib sau này

Không có wrapper riêng như `Avatar.tsx` (avatar-libs.md) — mỗi screen tự
import icon trực tiếp từ lib. Đổi lib nghĩa là đổi import ở từng file dùng
icon (`grep -rn "from \"lucide-react\""` để liệt kê hết chỗ cần sửa). Nếu
project sau này dùng nhiều icon và muốn đổi lib dễ hơn, cân nhắc làm lại kiểu
`src/icons.tsx` cũ: 1 file re-export icon cần dùng dưới tên riêng của mình,
mọi nơi khác import từ đó thay vì thẳng từ lib.
