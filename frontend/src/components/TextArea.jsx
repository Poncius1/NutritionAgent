function TextArea({ label, id, helperText, required, ...props }) {
  return (
    <div className="space-y-1 col-span-1 md:col-span-2">
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
      <textarea
        id={id}
        rows={3}
        className="block w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-nutrition-blue focus:border-nutrition-blue bg-white resize-none"
        {...props}
      />
    </div>
  );
}

export default TextArea;