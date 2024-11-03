import { useState, useEffect, useRef } from "react";
import { Link, useHistory } from "react-router-dom";
import VuiBox from "components/VuiBox";
import VuiTypography from "components/VuiTypography";
import VuiInput from "components/VuiInput";
import VuiButton from "components/VuiButton";
import VuiSwitch from "components/VuiSwitch";
import GradientBorder from "examples/GradientBorder";
import radialGradient from "assets/theme/functions/radialGradient";
import palette from "assets/theme/base/colors";
import borders from "assets/theme/base/borders";
import CoverLayout from "layouts/authentication/components/CoverLayout";
import bgSignIn from "assets/images/signUpImage.png";
import axios from "axios";
import { gsap } from "gsap";

function VolunteerSignUp() {
  const [rememberMe, setRememberMe] = useState(true);
  const handleSetRememberMe = () => setRememberMe(!rememberMe);

  const [formData, setFormData] = useState({
    email: "",
    password: "",
    name: "",
    phone_number: "",
    profile_picture: "",
    skills: [],
    availability: {},
    profile_urls: {},
    bio: "",
  });

  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const history = useHistory();
  
  // Create refs for input fields
  const inputRefs = useRef([]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSkillsChange = (e) => {
    setFormData({ ...formData, skills: e.target.value.split(',').map(skill => skill.trim()) });
  };

  const handleAvailabilityChange = (e) => {
    const [day, time] = e.target.name.split('_');
    setFormData({
      ...formData,
      availability: {
        ...formData.availability,
        [day]: { ...formData.availability[day], [time]: e.target.checked }
      }
    });
  };

  const handleProfileUrlsChange = (e) => {
    const [platform, url] = e.target.value.split(':');
    setFormData({
      ...formData,
      profile_urls: { ...formData.profile_urls, [platform.trim()]: url.trim() }
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError("");
    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/api/volunteer/signup`, formData);
      console.log("Signup successful:", response.data);
      localStorage.setItem("user", JSON.stringify(response.data.user));
      history.push("/profile");
    } catch (err) {
      setError(err.response?.data?.message || "An error occurred during signup. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    // Animate input fields on mount with reduced delay and duration
    gsap.from(inputRefs.current, {
      opacity: 0,
      y: 50,
      stagger: 0.1,
      duration: 0.3, // Reduced duration
      delay: 0, // No delay before starting the animation
      ease: "power3.out",
    });
  
    // Optional: If you want to animate the background image too
    gsap.from(".cover-image", {
      opacity: 0,
      scale: 1.1,
      duration: 0.5,
      ease: "power3.out",
      delay: 0.2, // Slightly after input fields
    });
  }, []);

  return (
    <CoverLayout
      title="Welcome, Volunteer!"
      description="Enter your details to sign up"
      image={bgSignIn}
    >
      <VuiBox component="form" role="form" onSubmit={handleSubmit}>
        {['name', 'email', 'password', 'phone_number', 'skills', 'profile_urls', 'bio'].map((field, index) => (
          <VuiBox mb={2} key={field} ref={el => inputRefs.current[index] = el}>
            <VuiBox mb={1} ml={0.5}>
              <VuiTypography component="label" variant="button" color="white" fontWeight="medium">
                {field.charAt(0).toUpperCase() + field.slice(1).replace(/_/g, ' ')}
              </VuiTypography>
            </VuiBox>
            <GradientBorder
              minWidth="100%"
              padding="1px"
              borderRadius={borders.borderRadius.lg}
              backgroundImage={radialGradient(
                palette.gradients.borderLight.main,
                palette.gradients.borderLight.state,
                palette.gradients.borderLight.angle
              )}
            >
              <VuiInput
                type={field === 'password' ? 'password' : (field === 'email' ? 'email' : 'text')}
                name={field}
                placeholder={`Your ${field.replace(/_/g, ' ')}...`}
                value={formData[field]}
                onChange={field === 'skills' ? handleSkillsChange : handleChange}
                fontWeight="500"
              />
            </GradientBorder>
          </VuiBox>
        ))}

        {/* Availability */}
        <VuiBox mb={2} ref={el => inputRefs.current[6] = el}>
          <VuiBox mb={1} ml={0.5}>
            <VuiTypography component="label" variant="button" color="white" fontWeight="medium">
              Availability
            </VuiTypography>
          </VuiBox>
          {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].map((day) => (
            <VuiBox key={day} display="flex" alignItems="center" mb={1}>
              <VuiTypography variant="button" fontWeight="regular" color="text" sx={{ minWidth: '100px' }}>
                {day}:
              </VuiTypography>
              <VuiBox display="flex">
                <VuiSwitch
                  name={`${day.toLowerCase()}_morning`}
                  checked={formData.availability[day.toLowerCase()]?.morning || false}
                  onChange={handleAvailabilityChange}
                />
                <VuiTypography variant="button" fontWeight="regular" color="text" sx={{ mx: 1 }}>
                  Morning
                </VuiTypography>
                <VuiSwitch
                  name={`${day.toLowerCase()}_afternoon`}
                  checked={formData.availability[day.toLowerCase()]?.afternoon || false}
                  onChange={handleAvailabilityChange}
                />
                <VuiTypography variant="button" fontWeight="regular" color="text" sx={{ mx: 1 }}>
                  Afternoon
                </VuiTypography>
                <VuiSwitch
                  name={`${day.toLowerCase()}_evening`}
                  checked={formData.availability[day.toLowerCase()]?.evening || false}
                  onChange={handleAvailabilityChange}
                />
                <VuiTypography variant="button" fontWeight="regular" color="text" sx={{ ml: 1 }}>
                  Evening
                </VuiTypography>
              </VuiBox>
            </VuiBox>
          ))}
        </VuiBox>

        {/* Remember Me Switch */}
        <VuiBox display="flex" alignItems="center" ref={el => inputRefs.current[7] = el}>
          <VuiSwitch color="info" checked={rememberMe} onChange={handleSetRememberMe} />
          <VuiTypography
            variant="caption"
            color="white"
            fontWeight="medium"
            onClick={handleSetRememberMe}
            sx={{ cursor: "pointer", userSelect: "none" }}
          >
            &nbsp;&nbsp;&nbsp;&nbsp;Remember me
          </VuiTypography>
        </VuiBox>

        {/* Sign Up Button */}
        <VuiBox mt={4} mb={1}>
          <VuiButton color="info" fullWidth type="submit" disabled={isLoading}>
            {isLoading ? "Signing Up..." : "SIGN UP"}
          </VuiButton>
        </VuiBox>
      </VuiBox>
    </CoverLayout>
  );
}

export default VolunteerSignUp;
