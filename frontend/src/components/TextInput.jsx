function TextInput({
  label,
  id,
  helperText,
  required,
  ...props
}) {
  return (
    <div className="space-y-1 col-span-1">
      <label
        htmlFor={id}
        className="block text-sm font-medium text-gray-700"
      >
        {label}
        {required && <span className="text-nutrition-orange"> *</span>}
      </label>
      {helperText && (
        <p className="text-xs text-gray-400 mb-1">{helperText}</p>
      )}
      <input
        id={id}
        className="block w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-nutrition-blue focus:border-nutrition-blue bg-white"
        {...props}
      />
    </div>
  );
}

export default TextInput;